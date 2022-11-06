import gettext
import os
import re
from datetime import datetime, timedelta
from importlib import import_module
from unittest import skipUnless

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.admin import widgets
from django.contrib.admin.tests import AdminSeleniumTestCase
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import (
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    UUIDField,
)
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse
from django.utils import translation

from .models import (
    Advisor,
    Album,
    Band,
    Bee,
    Car,
    Company,
    Event,
    Honeycomb,
    Image,
    Individual,
    Inventory,
    Member,
    MyFileField,
    Profile,
    ReleaseEvent,
    School,
    Student,
    UnsafeLimitChoicesTo,
    VideoStream,
)
from .widgetadmin import site as widget_admin_site


class TestDataMixin:
    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username="super", password="secret", email=None
        )
        cls.u2 = User.objects.create_user(username="testser", password="secret")
        Car.objects.create(owner=cls.superuser, make="Volkswagen", model="Passat")
        Car.objects.create(owner=cls.u2, make="BMW", model="M3")
