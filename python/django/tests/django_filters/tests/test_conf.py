from unittest import mock

from django.test import TestCase, override_settings

from django_filters.conf import is_callable, settings


class DefaultSettingsTests(TestCase):
    def test_verbose_lookups(self):
        self.assertIsInstance(settings.VERBOSE_LOOKUPS, dict)
        self.assertIn("exact", settings.VERBOSE_LOOKUPS)

    def test_default_lookup_expr(self):
        self.assertEqual(settings.DEFAULT_LOOKUP_EXPR, "exact")

    def test_disable_help_text(self):
        self.assertFalse(settings.DISABLE_HELP_TEXT)

    def test_empty_choice_label(self):
        self.assertEqual(settings.EMPTY_CHOICE_LABEL, "---------")

    def test_null_choice_label(self):
        self.assertIsNone(settings.NULL_CHOICE_LABEL)

    def test_null_choice_value(self):
        self.assertEqual(settings.NULL_CHOICE_VALUE, "null")
