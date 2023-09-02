import datetime
from copy import deepcopy

from django.core.exceptions import FieldError, MultipleObjectsReturned
from django.db import IntegrityError, models, transaction
from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from .models import (
    Article,
    Category,
    Child,
    ChildNullableParent,
    ChildStringPrimaryKeyParent,
    City,
    Country,
    District,
    First,
    Parent,
    ParentStringPrimaryKey,
    Record,
    Relation,
    Reporter,
    School,
    Student,
    Third,
    ToFieldChild,
    )

class ManyToOneTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a few Repoters.
        cls.r = Reporter(first_name="John", last_name="Smith", email="john@example.com")
        cls.r.save()
        cls.r2 = Reporter(first_name="Paul", last_name="Jones", email="paul@example.com")
        cls.r2.save()
        # Create an Article.
        cls.a =Article(
                headline="This is a test",
                pub_date=datetime.date(2005, 7, 27),
                reporter=cls.r,)
        cls.a.save()

    def test_get(self):
        # Article objects have access to their related Reporter objects.
        r = self.a.reporter
        self.assertEqual(r.id, self.r.id)
        self.assertEqual((r.first_name, self.r.last_name), ("John", "Smith"))
        
