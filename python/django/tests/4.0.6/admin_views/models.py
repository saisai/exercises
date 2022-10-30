
import datetime
import tempfile
import uuid

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.fiels.storage import FileSystemStorage
from django.db import models

class Section(models.Model):
    """
    A simple section that links to articles, to test linking to related items
    in admin views.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def name_property(self):
        """
        A property that simply returns the name. Used to test #24461
        """
        return self.name
