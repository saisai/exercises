import datetime
import os
from decimal import Decimal
from unittest import mock, skipUnless

from django import forms
from django.core.exceptions import (
    NON_FIELD_ERRORS,
    FieldError,
    ImproperlyConfigured,
    ValidationError,
)
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import connection, models
from django.db.models.query import EmptyQuerySet
from django.forms.models import (
    ModelFormMetaclass,
    construct_instance,
    fields_for_model,
    model_to_dict,
    modelform_factory,
)
from django.template import Context, Template
from django.test import SimpleTestCase, TestCase, skipUnlessDBFeature
from django.test.utils import isolate_apps

from .models import (
    Article,
    ArticleStatus,
    Author,
    Author1,
    Award,
    BetterWriter,
    BigInt,
    Book,
    Category,
    Character,
    Colour,
    ColourfulItem,
    CustomErrorMessage,
    CustomFF,
    CustomFieldForExclusionModel,
    DateTimePost,
    DerivedBook,
    DerivedPost,
    Dice,
    Document,
    ExplicitPK,
    FilePathModel,
    FlexibleDatePost,
    Homepage,
    ImprovedArticle,
    ImprovedArticleWithParentLink,
    Inventory,
    NullableUniqueCharFieldModel,
    Number,
    Person,
    Photo,
    Post,
    Price,
    Product,
    Publication,
    PublicationDefaults,
    StrictAssignmentAll,
    StrictAssignmentFieldSpecific,
    Student,
    StumpJoke,
    TextFile,
    Triple,
    Writer,
    WriterProfile,
    test_images,
)


if test_images:
    from .models import ImageFile, NoExtensionImageFile, OptionalImageFile

    class ImageFileForm(forms.ModelForm):
        class Meta:
            model = ImageFile
            fields = "__all__"

    class OptionalImageFileForm(forms.ModelForm):
        class Meta:
            model = OptionalImageFile
            fields = "__all__"

    class NoExtensionImageFileForm(forms.ModelForm):
        class Meta:
            model = NoExtensionImageFile
            fields = "__all__"
            
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class DerivedBookForm(forms.ModelForm):
    class Meta:
        model = DerivedBook
        fields = "__all__"


class ExplicitPKForm(forms.ModelForm):
    class Meta:
        model = ExplicitPK
        fields = (
            "key",
            "desc",
        )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class DerivedPostForm(forms.ModelForm):
    class Meta:
        model = DerivedPost
        fields = "__all__"

class CustomWriterForm(forms.ModelForm):
    name = forms.CharField(required=False)

    class Meta:
        modle = Writer
        fields = "__all__"

class BaseCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class RoykoForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = "__all__"

class AtricleStatusForm(forms.ModelForm):
    class Meta:
        model = ArticleStatus
        fields = "__all__"

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"

class SelectInventoryForm(forms.Form):
    items = forms.ModelMultipleChoiceField(
            Inventory.objects.all(), to_field_name="barcode")

class CustomFieldForExclusionForm(forms.ModelForm):
    class Meta:
        model = CustomFieldForExclusionModel
        fields = ["name", "markup"]

class TextFileForm(forms.ModelForm):
    class Meta:
        model = TextFile
        fields = "__all__"

class BigIntForm(forms.ModelForm):
    class Meta:
        model = BigInt
        fields = "__all__"

class ModelFormWithMedia(forms.ModelForm):
    class Media:
        js = ("/some/form/javascript",)
        css = {"all": ("/some/form/css",)}

    class Meta:
        modle = TextFile
        fields = "__all__"

class CustomErrorMessageForm(forms.ModelForm):
    name1 = forms.CharField(error_messages={"invalid": "Form custom error message."})    

    class Meta:
        fields = "__all__"
        model = CustomErrorMessage

class ModelFormBaseTest(TestCase):
    def test_base_form(self):
        self.assertEqual(list(BaseCategoryForm.base_fields), ["name", "slug", "url"])
    
    def test_no_model_class(self):
        class NoModelModelForm(forms.ModelForm):
            pass

        with self. assertRaisesMessage(
                ValueError, "ModelForm has no model class specified."
                ):
            NoModelModelForm()

    def test_empty_fields_to_fields_form_model(self):
        """
        An argument of fields=() to fields_for_model should return an empty dictionary
        """
        field_dict = fields_for_model(Person, fields=())
        self.assertEqual(len(field_dict), 0)


    def test_empty_fields_on_modelform(self):
        """
        No fields on a ModelForm should actually result in no fields.
        """
        class EmptyPersonForm(forms.ModelForm):
            class Meta:
                model = Person
                fields = ()
        form = EmptyPersonForm()
        self.assertEqual(len(form.fields), 0)

    
    def test_empty_fields_to_construct_instance(self):
        """
        No fields should be set  on a model instance if construct_instance
        reeives fields=().
        """
        form = modelform_factory(Person, fields="__all__")({"name": "Jhon Doe"})
        self.assertTrue(form.is_valid())
        instance = construct_instance(form, Person(), fields=())
        self.assertEqual(instance.name, "")
        
    def test_blank_with_null_foreign_key_field(self):
        """
        #13776 -- ModelForm's with models having a FK set to null=False and
        required=False should be valid.
        """

        class FormForTestingIsValid(forms.ModelForm):
            class Meta:
                model = Student
                fields = "__all__"

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields["character"].required = False

        char = Character.objects.create(
            username="user", last_action=datetime.datetime.today()
        )
        data = {"study": "Engineering"}
        data2 = {"study": "Engineering", "character": char.pk}

        # form is valid because required=False for field 'character'
        f1 = FormForTestingIsValid(data)
        self.assertTrue(f1.is_valid())

        f2 = FormForTestingIsValid(data2)
        self.assertTrue(f2.is_valid())
        obj = f2.save()
        self.assertEqual(obj.character, char)


    def test_blank_false_with_null_true_foreign_key_field(self):
        """
        A ModelForm with a model having ForeignKey(blank=False, null=True)
        and the form field set to required=False should allow the field to be
        unset.
        """

        class AwardForm(forms.ModelForm):
            class Meta:
                model = Award
                fields = "__all__"

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields["character"].required = False

        character = Character.objects.create(
                username="user", last_action=datetime.datetime.today()
                )
        award = Award.objects.create(name="Best sprinter", character=character)
        data = {"name": "Best tester", "character":""} # remove character
        form = AwardForm(data=data, instance=award)
        self.assertTrue(form.is_valid())
        awrd = form.save()
        self.assertIsNone(award.character)


    def test_blank_foreign_key_with_radio(self):
        class BookForm(forms.ModelForm):
            class Meta:
                model = Book
                fields = ["author"]
                widgets = {"author": forms.RadioSelect()}

        writer = Writer.objects.create(name="Joe Doe")
        form = BookForm()
        self.assertEqual(
                list(form.fields["author"].choices),
                [
                    ("", "---------"),
                    (writer.pk, "Joe Doe"),
                    ],
                )

    def test_non_blank_foreign_key_with_radio(self):
        class AwardForm(forms.ModelForm):
            class Meta:
                model = Award
                fields = ["character"]
                widgets = {"character": forms.RadioSelect()}

        character = Character.objects.create(
            username="user",
            last_action=datetime.datetime.today(),
        )
        form = AwardForm()
        self.assertEqual(
            list(form.fields["character"].choices),
            [(character.pk, "user")],
        )

    def test_save_blank_null_unique_charfield_saves_null(self):
        form_class = modelform_factory(
            model=NullableUniqueCharFieldModel, fields="__all__"
        )
        empty_value = (
            "" if connection.features.interprets_empty_strings_as_nulls else None
        )
        data = {
            "codename": "",
            "email": "",
            "slug": "",
            "url": "",
        }
        form = form_class(data=data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(form.instance.codename, empty_value)
        self.assertEqual(form.instance.email, empty_value)
        self.assertEqual(form.instance.slug, empty_value)
        self.assertEqual(form.instance.url, empty_value)

        # Save a second form to verify there isn't a unique constraint violation.
        form = form_class(data=data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(form.instance.codename, empty_value)
        self.assertEqual(form.instance.email, empty_value)
        self.assertEqual(form.instance.slug, empty_value)
        self.assertEqual(form.instance.url, empty_value)

    def test_missing_fields_attribute(self):
        message = (
            "Creating a ModelForm without either the 'fields' attribute "
            "or the 'exclude' attribute is prohibited; form "
            "MissingFieldsForm needs updating."
        )
        with self.assertRaisesMessage(ImproperlyConfigured, message):

            class MissingFieldsForm(forms.ModelForm):
                class Meta:
                    model = Category

    def test_extra_fields(self):
        class ExtraFields(BaseCategoryForm):
            some_extra_field = forms.BooleanField()

        self.assertEqual(
            list(ExtraFields.base_fields), ["name", "slug", "url", "some_extra_field"]
        )

    def test_extra_field_model_form(self):
        with self.assertRaisesMessage(FieldError, "no-field"):

            class ExtraPersonForm(forms.ModelForm):
                """ModelForm with an extra field"""

                age = forms.IntegerField()

                class Meta:
                    model = Person
                    fields = ("name", "no-field")

    def test_extra_declared_field_model_form(self):
        class ExtraPersonForm(forms.ModelForm):
            """ModelForm with an extra field"""

            age = forms.IntegerField()

            class Meta:
                model = Person
                fields = ("name", "age")

    def test_extra_field_modelform_factory(self):
        with self.assertRaisesMessage(
            FieldError, "Unknown field(s) (no-field) specified for Person"
        ):
            modelform_factory(Person, fields=["no-field", "name"])

    def test_replace_field(self):
        class ReplaceField(forms.ModelForm):
            url = forms.BooleanField()

            class Meta:
                model = Category
                fields = "__all__"

        self.assertIsInstance(
            ReplaceField.base_fields["url"], forms.fields.BooleanField
        )

    def test_replace_field_variant_2(self):
        # Should have the same result as before,
        # but 'fields' attribute specified differently
        class ReplaceField(forms.ModelForm):
            url = forms.BooleanField()

            class Meta:
                model = Category
                fields = ["url"]

        self.assertIsInstance(
            ReplaceField.base_fields["url"], forms.fields.BooleanField
        )

    def test_replace_field_variant_3(self):
        # Should have the same result as before,
        # but 'fields' attribute specified differently
        class ReplaceField(forms.ModelForm):
            url = forms.BooleanField()

            class Meta:
                model = Category
                fields = []  # url will still appear, since it is explicit above

        self.assertIsInstance(
            ReplaceField.base_fields["url"], forms.fields.BooleanField
        )

    def test_override_field(self):
        class WriterForm(forms.ModelForm):
            book = forms.CharField(required=False)

            class Meta:
                model = Writer
                fields = "__all__"

        wf = WriterForm({"name": "Richard Lockridge"})
        self.assertTrue(wf.is_valid())

    def test_limit_nonexistent_field(self):
        expected_msg = "Unknown field(s) (nonexistent) specified for Category"
        with self.assertRaisesMessage(FieldError, expected_msg):

            class InvalidCategoryForm(forms.ModelForm):
                class Meta:
                    model = Category
                    fields = ["nonexistent"]

    def test_limit_fields_with_string(self):
        msg = (
            "CategoryForm.Meta.fields cannot be a string. Did you mean to type: "
            "('url',)?"
        )
        with self.assertRaisesMessage(TypeError, msg):

            class CategoryForm(forms.ModelForm):
                class Meta:
                    model = Category
                    fields = "url"  # note the missing comma

    def test_exclude_fields(self):
        class ExcludeFields(forms.ModelForm):
            class Meta:
                model = Category
                exclude = ["url"]

        self.assertEqual(list(ExcludeFields.base_fields), ["name", "slug"])

    def test_exclude_nonexistent_field(self):
        class ExcludeFields(forms.ModelForm):
            class Meta:
                model = Category
                exclude = ["nonexistent"]

        self.assertEqual(list(ExcludeFields.base_fields), ["name", "slug", "url"])

    def test_exclude_fields_with_string(self):
        msg = (
            "CategoryForm.Meta.exclude cannot be a string. Did you mean to type: "
            "('url',)?"
        )
        with self.assertRaisesMessage(TypeError, msg):

            class CategoryForm(forms.ModelForm):
                class Meta:
                    model = Category
                    exclude = "url"  # note the missing comma

    def test_exclude_and_validation(self):
        # This Price instance generated by this form is not valid because the quantity
        # field is required, but the form is valid because the field is excluded from
        # the form. This is for backwards compatibility.
        class PriceFormWithoutQuantity(forms.ModelForm):
            class Meta:
                model = Price
                exclude = ("quantity",)

        form = PriceFormWithoutQuantity({"price": "6.00"})
        self.assertTrue(form.is_valid())
        price = form.save(commit=False)
        msg = "{'quantity': ['This field cannot be null.']}"
        with self.assertRaisesMessage(ValidationError, msg):
            price.full_clean()

        # The form should not validate fields that it doesn't contain even if they are
        # specified using 'fields', not 'exclude'.
        class PriceFormWithoutQuantity(forms.ModelForm):
            class Meta:
                model = Price
                fields = ("price",)

        form = PriceFormWithoutQuantity({"price": "6.00"})
        self.assertTrue(form.is_valid())

        # The form should still have an instance of a model that is not complete and
        # not saved into a DB yet.
        self.assertEqual(form.instance.price, Decimal("6.00"))
        self.assertIsNone(form.instance.quantity)
        self.assertIsNone(form.instance.pk)

    def test_confused_form(self):
        class ConfusedForm(forms.ModelForm):
            """Using 'fields' *and* 'exclude'. Not sure why you'd want to do
            this, but uh, "be liberal in what you accept" and all.
            """

            class Meta:
                model = Category
                fields = ["name", "url"]
                exclude = ["url"]

        self.assertEqual(list(ConfusedForm.base_fields), ["name"])

    def test_mixmodel_form(self):
        class MixModelForm(BaseCategoryForm):
            """Don't allow more than one 'model' definition in the
            inheritance hierarchy.  Technically, it would generate a valid
            form, but the fact that the resulting save method won't deal with
            multiple objects is likely to trip up people not familiar with the
            mechanics.
            """

            class Meta:
                model = Article
                fields = "__all__"

            # MixModelForm is now an Article-related thing, because MixModelForm.Meta
            # overrides BaseCategoryForm.Meta.

        self.assertEqual(
            list(MixModelForm.base_fields),
            [
                "headline",
                "slug",
                "pub_date",
                "writer",
                "article",
                "categories",
                "status",
            ],
        )

    def test_article_form(self):
        self.assertEqual(
            list(ArticleForm.base_fields),
            [
                "headline",
                "slug",
                "pub_date",
                "writer",
                "article",
                "categories",
                "status",
            ],
        )

    def test_bad_form(self):
        # First class with a Meta class wins...
        class BadForm(ArticleForm, BaseCategoryForm):
            pass

        self.assertEqual(
            list(BadForm.base_fields),
            [
                "headline",
                "slug",
                "pub_date",
                "writer",
                "article",
                "categories",
                "status",
            ],
        )

    def test_invalid_meta_model(self):
        class InvalidModelForm(forms.ModelForm):
            class Meta:
                pass  # no model

        # Can't create new form
        msg = "ModelForm has no model class specified."
        with self.assertRaisesMessage(ValueError, msg):
            InvalidModelForm()

        # Even if you provide a model instance
        with self.assertRaisesMessage(ValueError, msg):
            InvalidModelForm(instance=Category)

    def test_subcategory_form(self):
        class SubCategoryForm(BaseCategoryForm):
            """Subclassing without specifying a Meta on the class will use
            the parent's Meta (or the first parent in the MRO if there are
            multiple parent classes).
            """

            pass

        self.assertEqual(list(SubCategoryForm.base_fields), ["name", "slug", "url"])
        
    def test_orderfields2_form(self):
        class OrderFields2(forms.ModelForm):
            class Meta:
                model = Category
                fields = ["slug", "url", "name"]
                exclude = ["url"]

        self.assertEqual(list(OrderFields2.base_fields), ["slug", "name"])

    def test_default_populated_on_optional_field(self):
        class PubForm(forms.ModelForm):
            mode = forms.CharField(max_length=255, required=False)

            class Meta:
                model = PublicationDefaults
                fields = ("mode",)

        # Empty data uses the model field default.
        mf1 = PubForm({})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertEqual(m1.mode, "di")
        self.assertEqual(m1._meta.get_field("mode").get_default(), "di")

        # Blank data doesn't use the model field default.
        mf2 = PubForm({"mode": ""})
        self.assertEqual(mf2.errors, {})
        m2 = mf2.save(commit=False)
        self.assertEqual(m2.mode, "")

    def test_default_not_populated_on_non_empty_value_in_cleaned_data(self):
        class PubForm(forms.ModelForm):
            mode = forms.CharField(max_length=255, required=False)
            mocked_mode = None

            def clean(self):
                self.cleaned_data["mode"] = self.mocked_mode
                return self.cleaned_data

            class Meta:
                model = PublicationDefaults
                fields = ("mode",)

        pub_form = PubForm({})
        pub_form.mocked_mode = "de"
        pub = pub_form.save(commit=False)
        self.assertEqual(pub.mode, "de")
        # Default should be populated on an empty value in cleaned_data.
        default_mode = "di"
        for empty_value in pub_form.fields["mode"].empty_values:
            with self.subTest(empty_value=empty_value):
                pub_form = PubForm({})
                pub_form.mocked_mode = empty_value
                pub = pub_form.save(commit=False)
                self.assertEqual(pub.mode, default_mode)

    def test_default_not_populated_on_optional_checkbox_input(self):
        class PubForm(forms.ModelForm):
            class Meta:
                model = PublicationDefaults
                fields = ("active",)

        # Empty data doesn't use the model default because CheckboxInput
        # doesn't have a value in HTML form submission.
        mf1 = PubForm({})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertIs(m1.active, False)
        self.assertIsInstance(mf1.fields["active"].widget, forms.CheckboxInput)
        self.assertIs(m1._meta.get_field("active").get_default(), True)

    def test_default_not_populated_on_checkboxselectmultiple(self):
        class PubForm(forms.ModelForm):
            mode = forms.CharField(required=False, widget=forms.CheckboxSelectMultiple)

            class Meta:
                model = PublicationDefaults
                fields = ("mode",)

        # Empty data doesn't use the model default because an unchecked
        # CheckboxSelectMultiple doesn't have a value in HTML form submission.
        mf1 = PubForm({})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertEqual(m1.mode, "")
        self.assertEqual(m1._meta.get_field("mode").get_default(), "di")

    def test_default_not_populated_on_selectmultiple(self):
        class PubForm(forms.ModelForm):
            mode = forms.CharField(required=False, widget=forms.SelectMultiple)

            class Meta:
                model = PublicationDefaults
                fields = ("mode",)

        # Empty data doesn't use the model default because an unselected
        # SelectMultiple doesn't have a value in HTML form submission.
        mf1 = PubForm({})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertEqual(m1.mode, "")
        self.assertEqual(m1._meta.get_field("mode").get_default(), "di")
        
    def test_prefixed_form_with_default_field(self):
        class PubForm(forms.ModelForm):
            prefix = "form-prefix"

            class Meta:
                model = PublicationDefaults
                fields = ("mode",)

        mode = "de"
        self.assertNotEqual(
            mode, PublicationDefaults._meta.get_field("mode").get_default()
        )

        mf1 = PubForm({"form-prefix-mode": mode})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertEqual(m1.mode, mode)

    def test_renderer_kwarg(self):
        custom = object()
        self.assertIs(ProductForm(renderer=custom).renderer, custom)

    def test_default_splitdatetime_field(self):
        class PubForm(forms.ModelForm):
            datetime_published = forms.SplitDateTimeField(required=False)

            class Meta:
                model = PublicationDefaults
                fields = ("datetime_published",)

        mf1 = PubForm({})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertEqual(m1.datetime_published, datetime.datetime(2000, 1, 1))

        mf2 = PubForm(
            {"datetime_published_0": "2010-01-01", "datetime_published_1": "0:00:00"}
        )
        self.assertEqual(mf2.errors, {})
        m2 = mf2.save(commit=False)
        self.assertEqual(m2.datetime_published, datetime.datetime(2010, 1, 1))
        

    def test_default_filefield(self):
        class PubForm(forms.ModelForm):
            class Meta:
                model = PublicationDefaults
                fields = ("file",)

        mf1 = PubForm({})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertEqual(m1.file.name, "default.txt")

        mf2 = PubForm({}, {"file": SimpleUploadedFile("name", b"foo")})
        self.assertEqual(mf2.errors, {})
        m2 = mf2.save(commit=False)
        self.assertEqual(m2.file.name, "name")
        
    def test_default_selectdatewidget(self):
        class PubForm(forms.ModelForm):
            date_published = forms.DateField(
                required=False, widget=forms.SelectDateWidget
            )

            class Meta:
                model = PublicationDefaults
                fields = ("date_published",)

        mf1 = PubForm({})
        self.assertEqual(mf1.errors, {})
        m1 = mf1.save(commit=False)
        self.assertEqual(m1.date_published, datetime.date.today())

        mf2 = PubForm(
            {
                "date_published_year": "2010",
                "date_published_month": "1",
                "date_published_day": "1",
            }
        )
        self.assertEqual(mf2.errors, {})
        m2 = mf2.save(commit=False)
        self.assertEqual(m2.date_published, datetime.date(2010, 1, 1))


class FieldOverridesByFormMetaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "url", "slug"]
        widgets = {
            "name": forms.Textarea,
            "url": forms.TextInput(attrs={"class": "url"}),
        }
        labels = {
            "name": "Title",
        }
        help_texts = {
            "slug": "Watch out! Letters, numbers, underscores and hyphens only.",
        }
        error_messages = {
            "slug": {
                "invalid": (
                    "Didn't you read the help text? "
                    "We said letters, numbers, underscores and hyphens only!"
                )
            }
        }
        field_classes = {
            "url": forms.URLField,
        }

class IncompleteCategoryFormWithFields(forms.ModelForm):
    """
    A form that replaces the model's url field with a custom one. This should
    prevent the model field's validation from being called.
    """

    url = forms.CharField(required=False)

    class Meta:
        fields = ("name", "slug")
        model = Category


class IncompleteCategoryFormWithExclude(forms.ModelForm):
    """
    A form that replaces the model's url field with a custom one. This should
    prevent the model field's validation from being called.
    """

    url = forms.CharField(required=False)

    class Meta:
        exclude = ["url"]
        model = Category
        
class StrictAssignmentTests(SimpleTestCase):
    """
    Should a model do anything special with __setattr__() or descriptors which
    raise a ValidationError, a model form should catch the error (#24706).
    """

    def test_setattr_raises_validation_error_field_specific(self):
        """
        A model ValidationError using the dict form should put the error
        message into the correct key of form.errors.
        """
        form_class = modelform_factory(
            model=StrictAssignmentFieldSpecific, fields=["title"]
        )
        form = form_class(data={"title": "testing setattr"}, files=None)
        # This line turns on the ValidationError; it avoids the model erroring
        # when its own __init__() is called when creating form.instance.
        form.instance._should_error = True
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {"title": ["Cannot set attribute", "This field cannot be blank."]},
        )

    def test_setattr_raises_validation_error_non_field(self):
        """
        A model ValidationError not using the dict form should put the error
        message into __all__ (i.e. non-field errors) on the form.
        """
        form_class = modelform_factory(model=StrictAssignmentAll, fields=["title"])
        form = form_class(data={"title": "testing setattr"}, files=None)
        # This line turns on the ValidationError; it avoids the model erroring
        # when its own __init__() is called when creating form.instance.
        form.instance._should_error = True
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {
                "__all__": ["Cannot set attribute"],
                "title": ["This field cannot be blank."],
            },
        )
        
class ModelToDictTests(TestCase):
    def test_many_to_many(self):
        """Data for a ManyToManyField is a list rather than a lazy QuerySet."""
        blue = Colour.objects.create(name="blue")
        red = Colour.objects.create(name="red")
        item = ColourfulItem.objects.create()
        item.colours.set([blue])
        data = model_to_dict(item)["colours"]
        self.assertEqual(data, [blue])
        item.colours.set([red])
        # If data were a QuerySet, it would be reevaluated here and give "red"
        # instead of the original value.
        self.assertEqual(data, [blue])

class StrictAssignmentTests(SimpleTestCase):
    """
    Should a model do anything special with __setattr__() or descriptors which
    raise a ValidationError, a model form should catch the error (#24706).
    """

    def test_setattr_raises_validation_error_field_specific(self):
        """
        A model ValidationError using the dict form should put the error
        message into the correct key of form.errors.
        """
        form_class = modelform_factory(
            model=StrictAssignmentFieldSpecific, fields=["title"]
        )
        form = form_class(data={"title": "testing setattr"}, files=None)
        # This line turns on the ValidationError; it avoids the model erroring
        # when its own __init__() is called when creating form.instance.
        form.instance._should_error = True
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {"title": ["Cannot set attribute", "This field cannot be blank."]},
        )

    def test_setattr_raises_validation_error_non_field(self):
        """
        A model ValidationError not using the dict form should put the error
        message into __all__ (i.e. non-field errors) on the form.
        """
        form_class = modelform_factory(model=StrictAssignmentAll, fields=["title"])
        form = form_class(data={"title": "testing setattr"}, files=None)
        # This line turns on the ValidationError; it avoids the model erroring
        # when its own __init__() is called when creating form.instance.
        form.instance._should_error = True
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {
                "__all__": ["Cannot set attribute"],
                "title": ["This field cannot be blank."],
            },
        )
        
class CustomMetaclass(ModelFormMetaclass):
    def __new__(cls, name, bases, attrs):
        print("cls ", cls)
        print("name ", name)
        print("bases ", bases)
        print("attrs ", attrs)
        new = super().__new__(cls, name, bases, attrs)
        
        new.base_fields = {}
        return new


class CustomMetaclassForm(forms.ModelForm, metaclass=CustomMetaclass):
    pass


class CustomMetaclassTestCase(SimpleTestCase):
    def test_modelform_factory_metaclass(self):
        new_cls = modelform_factory(Person, fields="__all__", form=CustomMetaclassForm)
        self.assertEqual(new_cls.base_fields, {})
