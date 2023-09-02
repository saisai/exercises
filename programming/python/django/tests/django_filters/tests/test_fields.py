import decimal
from datetime import datetime, time, timedelta, tzinfo

import pytz
from django import forms
from django.test import TestCase, override_settings
from django.utils import timezone

from django_filters.fields import (
    BaseCSVField,
    BaseRangeField,
    DateRangeField,
    DateTimeRangeField,
    IsoDateTimeField,
    IsoDateTimeRangeField,
    Lookup,
    LookupChoiceField,
    RangeField,
    TimeRangeField,
        )
from django_filters.widgets import BaseCSVWidget, CSVWidget, RangeWidget

def to_d(float_value):
    return decimal.Decimal("%.2f" % float_value)

class LooupTests(TestCase):
    def test_empty_attrs(self):
        with self.assertRaisesMessage(ValueError, ""):
            Lookup(None, None)

        with self.assertRaisesMessage(ValueError, ""):
            Lookup("", "")

    def test_empty_value(self):
        with self.assertRaisesMessage(ValueError, ""):
            Lookup("", "exact")

    def test_empty_lookup_expr(self):
        with self.assertRaisesMessage(ValueError, ""):
            Lookup("Value", "")

class RangeFieldTests(TestCase):
    def test_field(self):
        f = RangeField()
        self.assertEqual(len(f.fields), 2)

    def test_clean(self):
        w = RangeWidget()
        f = RangeField(widget=w, required=False)

        self.assertEqual(f.clean(["12.34", "55"]), slice(to_d(12.34), to_d(55)))
        self.assertIsNone(f.clean([]))
