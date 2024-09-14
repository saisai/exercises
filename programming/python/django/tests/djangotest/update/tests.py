import unittest 

from django.core.exceptions import FieldError
from django.db import IntegrityError, connection, transaction
from django.db.models import Case, CharField, Count, F, IntegerField, Max, When
from django.db.models.functions import Abs, Concat, Lower
from django.test import TestCase 
from django.test.utils import register_lookup 

from .models import (
    A,
    B,
    Bar,
    D,
    DataPoint,
    Foo,
    RelatedPoint,
    UniqueNumber,
    UniqueNumberChild,
)


class SimpleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.a1 = A.objects.create()
        cls.a2 = A.objects.create()
        for x in range(20):
            B.objects.create(a=cls.a1)
            D.objects.create(a=cls.a1)

    def test_nonempty_update(self):
        """
        Update changes the right number of rows for a nonempty queryset
        """
        num_updated = self.a1.b_set.update(y=100)
        self.assertEqual(num_updated, 20)
        cnt = B.objects.filter(y=100).count()
        self.assertEqual(cnt, 20)





