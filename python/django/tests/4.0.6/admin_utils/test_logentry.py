
import json
from datetime import datetime

from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.contrib.admin.utils import quote
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import translation
from django.utils.html import escape

from .models import Article, ArticleProxy, Site

@override_settings(ROOT_URLCONF="admin_utils.urls")
class LogEntryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser(
                username="super", password="secret", email="super@example.com"
                )
        cls.site = Site.objects.create(domain="example.org")
        cls.a1 = Article.objects.create(
                site=cls.site,
                title="Title",
                created=datetime(2008, 3, 12, 11, 54),
                )
        content_type_pk = ContentType.objects.get_for_model(Article).pk
        LogEntry.objects.log_action(
                cls.user.pk,
                content_type_pk,
                cls.a1.pk,
                repr(cls.a1),
                CHANGE,
                change_message="Changed something",
                )

    def setUp(self):
        self.client.force_login(self.user)

    def test_logentry_save(self):
        """
        LogEntry.action_time is a timestamp of the date when the entry was
        created. It shouldn't be upated on a subseqeunt save().
        """
        logentry = LogEntry.objects.get(content_type__model__iexact="article")
        action_time = logentry.action_time
        logentry.save()
        self.assertEqual(logentry.action_time, action_time)
    
    def test_logentry_change_message(self):
        """
        LogEntry.change_message is stored as a dumped JSON structure to be able
        to get the message dynamically translated at display time.
        """
        post_data = {
                "site" :self.site.pk,
                "title" : "Changed",
                "hist" : "Some content",
                "created_0": "2008-03-12",
                "created_1": "11:54",
                }
        change_url = reverse(
                "admin:admin_utils_article_change", args=[quote(self.a1.pk)]
                )
        response = self.client.post(change_url, post_data)
        self.assertRedirects(response, reverse("admin:admin_utils_article_changelist"))
        logentry = LogEntry.objects.filter(
                content_type__model__iexact="article"
                ).latest("id")
        self.assertEqual(logentry.get_change_message(), "Changed Title and History.")
        with translation.override("fr"):
            self.assertEqual(
                    logentry.get_change_message(), "Modification de Title et Historique."
                    )
        add_url = reverse("admin:admin_utils_article_add")
        post_data["title"] = "New"
        response = self.client.post(add_url, post_data)
        self.assertRedirects(response, reverse("admin:admin_utils_article_changelist"))
        logentry = LogEntry.objects.filter(
                content_type__model__iexact="article"
                ).latest("id")
        self.assertEqual(logentry.get_change_message(), "Added.")
        with translation.override("fr"):
            self.assertEqual(logentry.get_change_message(), "Ajout.")


    def test_logentry_change_message_not_json(self):
        """LogEntry.change_message was a string before Django 1.10."""
        logentry = LogEntry(change_message="non-JSON string")
        self.assertEqual(logentry.get_change_message(), logentry.change_message)


    def test_logentry_change_message_localized_datetime_input(self):
        """
        Localized date/time inputs shouldn't affetct changed form data detection.
        """
        post_data = {
                "site": self.site.pk,
                "title": "Changed",
                "hist": "Some content",
                "created_0": "12/03/2008",
                "created_1": "11:54",
                }
        with translation.override("fr"):
            change_url = reverse(
                    "admin:admin_utils_article_change", args=[quote(self.a1.pk)]
                    )
            response = self.client.post(change_url, post_data)
            self.assertRedirects(
                    response, reverse("admin:admin_utils_article_changelist")
                    )
        logentry = LogEntry.objects.filter(
                    content_type__model__iexact="article"
                    ).latest("id")
        self.assertEqual(logentry.get_change_message(), "Changed Title and History.")
            
