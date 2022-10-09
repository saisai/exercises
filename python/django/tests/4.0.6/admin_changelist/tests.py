import datetime

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.admin.tests import AdminSeleniumTestCase
from django.contrib.admin.views.main import (
    ALL_VAR,
    IS_POPUP_VAR,
    ORDER_VAR,
    PAGE_VAR,
    SEARCH_VAR,
    TO_FIELD_VAR,
)
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.storage.cookie import CookieStorage
from django.db import connection, models
from django.db.models import F, Field, IntegerField
from django.db.models.functions import Upper
from django.db.models.lookups import Contains, Exact
from django.template import Context, Template, TemplateSyntaxError
from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from django.test.utils import CaptureQueriesContext, isolate_apps, register_lookup
from django.urls import reverse
from django.utils import formats

from .admin import (
    BandAdmin,
    ChildAdmin,
    ChordsBandAdmin,
    ConcertAdmin,
    CustomPaginationAdmin,
    CustomPaginator,
    DynamicListDisplayChildAdmin,
    DynamicListDisplayLinksChildAdmin,
    DynamicListFilterChildAdmin,
    DynamicSearchFieldsChildAdmin,
    EmptyValueChildAdmin,
    EventAdmin,
    FilteredChildAdmin,
    GroupAdmin,
    InvitationAdmin,
    NoListDisplayLinksParentAdmin,
    ParentAdmin,
    ParentAdminTwoSearchFields,
    QuartetAdmin,
    SwallowAdmin,
)
from .admin import site as custom_site
from .models import (
    Band,
    CharPK,
    Child,
    ChordsBand,
    ChordsMusician,
    Concert,
    CustomIdUser,
    Event,
    Genre,
    Group,
    Invitation,
    Membership,
    Musician,
    OrderedObject,
    Parent,
    Quartet,
    Swallow,
    SwallowOneToOne,
    UnorderedObject,
)


def build_tbody_html(pk, href, extra_fields):
    return (
        "<tbody><tr>"
        '<td class="action-checkbox">'
        '<input type="checkbox" name="_selected_action" value="{}" '
        'class="action-select"></td>'
        '<th class="field-name"><a href="{}">name</a></th>'
        "{}</tr></tbody>"
    ).format(pk, href, extra_fields)


@override_settings(ROOT_URLCONF="admin_changelist.urls")
class ChangeListTests(TestCase):
    factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username="super", email="a@b.com", password="xxx"
        )

    def _create_superuser(self, username):
        return User.objects.create_superuser(
            username=username, email="a@b.com", password="xxx"
        )

    def _mocked_authenticated_request(self, url, user):
        request = self.factory.get(url)
        request.user = user
        return request

    def test_repr(self):
        m = ChildAdmin(Child, custom_site)
        
        def show_obj_dir():
            for obj in [f for f in dir(m) if not f.startswith('_')]:
                print(obj, "=>", getattr(m, obj))
                
        request = self.factory.get("/child/")
        request.user = self.superuser
        cl = m.get_changelist_instance(request)
        self.assertEqual(repr(cl), "<ChangeList: model=Child model_admin=ChildAdmin>")
        #print(repr(cl))

    def test_specified_ordering_by_f_expression(self):
        class OrderedByFBandAdmin(admin.ModelAdmin):
            list_display = ["name", "genres", "nr_of_members"]
            ordering = (
                F("nr_of_members").desc(nulls_last=True),
                Upper(F("name")).asc(),
                F("genres").asc(),
            )

        m = OrderedByFBandAdmin(Band, custom_site)
        request = self.factory.get("/band/")
        request.user = self.superuser
        cl = m.get_changelist_instance(request)
        
        def show_dir():                
            for obj in [f for f in dir(cl) if not f.startswith('_')]:
                try:
                    print(obj, "=> ", getattr(cl, obj)())
                except TypeError as e:
                    print(obj, "Error => ", getattr(cl, obj))
                finally:
                    print(obj, "Finally => ", getattr(cl, obj))
                    
    def test_select_related_preserved(self):
        """
        Regression test for #10348: ChangeList.get_queryset() shouldn't
        overwrite a custom select_related provided by ModelAdmin.get_queryset().
        """
        m = ChildAdmin(Child, custom_site)
        request = self.factory.get("/child/")
        request.user = self.superuser
        cl = m.get_changelist_instance(request)
        self.assertEqual(cl.queryset.query.select_related, {"parent": {}})

    def test_select_related_preserved_when_multi_valued_in_search_fields(self):
        parent = Parent.objects.create(name="Mary")
        Child.objects.create(parent=parent, name="Danielle")
        Child.objects.create(parent=parent, name="Daniel")

        m = ParentAdmin(Parent, custom_site)
        request = self.factory.get("/parent/", data={SEARCH_VAR: "daniel"})
        
        def show_dir_result():                
            for obj in [f for f in dir(request) if not f.startswith('_')]:
                print(obj, " => ", getattr(request, obj))
        
        request.user = self.superuser

        cl = m.get_changelist_instance(request)
        self.assertEqual(cl.queryset.count(), 1)
        # select_related is preserved.
        self.assertEqual(cl.queryset.query.select_related, {"child": {}})
        
    def test_select_related_as_tuple(self):
        ia = InvitationAdmin(Invitation, custom_site)
        request = self.factory.get("/invitation/")
        request.user = self.superuser
        cl = ia.get_changelist_instance(request)
        self.assertEqual(cl.queryset.query.select_related, {"player": {}})

    def test_select_related_as_empty_tuple(self):
        ia = InvitationAdmin(Invitation, custom_site)
        ia.list_select_related = ()
        request = self.factory.get("/invitation/")
        request.user = self.superuser
        cl = ia.get_changelist_instance(request)
        self.assertIs(cl.queryset.query.select_related, False)

    def test_get_select_related_custom_method(self):
        class GetListSelectRelatedAdmin(admin.ModelAdmin):
            list_display = ("band", "player")

            def get_list_select_related(self, request):
                return ("band", "player")

        ia = GetListSelectRelatedAdmin(Invitation, custom_site)
        request = self.factory.get("/invitation/")
        request.user = self.superuser
        cl = ia.get_changelist_instance(request)
        self.assertEqual(cl.queryset.query.select_related, {"player": {}, "band": {}})

    def test_many_search_terms(self):
        parent = Parent.objects.create(name="Mary")
        Child.objects.create(parent=parent, name="Danielle")
        Child.objects.create(parent=parent, name="Daniel")

        m = ParentAdmin(Parent, custom_site)
        request = self.factory.get("/parent/", data={SEARCH_VAR: "daniel " * 80})
        request.user = self.superuser

        cl = m.get_changelist_instance(request)
        with CaptureQueriesContext(connection) as context:
            object_count = cl.queryset.count()
        self.assertEqual(object_count, 1)
        self.assertEqual(context.captured_queries[0]["sql"].count("JOIN"), 1)

    def test_related_field_multiple_search_terms(self):
        """
        Searches over multi-valued relationships return rows from related
        models only when all searched fields match that row.
        """
        parent = Parent.objects.create(name="Mary")
        Child.objects.create(parent=parent, name="Danielle", age=18)
        Child.objects.create(parent=parent, name="Daniel", age=19)

        m = ParentAdminTwoSearchFields(Parent, custom_site)

        request = self.factory.get("/parent/", data={SEARCH_VAR: "danielle 19"})
        request.user = self.superuser
        cl = m.get_changelist_instance(request)
        self.assertEqual(cl.queryset.count(), 0)

        request = self.factory.get("/parent/", data={SEARCH_VAR: "daniel 19"})
        request.user = self.superuser
        cl = m.get_changelist_instance(request)
        self.assertEqual(cl.queryset.count(), 1)