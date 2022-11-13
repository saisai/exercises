import json
import xml.etree.ElementTree
from datetime import datetime

from asgiref.sync import async_to_sync, sync_to_async

from django.db import NotSupportedError, connection
from django.db.models import Sum
from django.test import TestCase, skipIfDBFeature, skipUnlessDBFeature

from .models import SimpleModel

class AsyncQuerySetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.s1 = SimpleModel.objects.create(
                field=1,
                created=datetime(2022, 1, 1, 0, 0, 0),
                )
        cls.s2 = SimpleModel.objects.create(
            field=2,
            created=datetime(2022, 1, 1, 0, 0, 1),
        )
        cls.s3 = SimpleModel.objects.create(
            field=3,
            created=datetime(2022, 1, 1, 0, 0, 2),
        )

    @staticmethod
    def _get_db_feature(connection_,feature_name):
        # Wrapper to avoid accessing connection attributes until inside
        # coroutine function. Connection access is thread sensitive and cannot
        # be passed across sync/async boundaries.
        return getattr(connection_.features, feature_name)

    async def test_async_iteration(self):
        results = []
        async for m in SimpleModel.objects.order_by("pk"):
            results.append(m)
        self.assertEqual(results, [self.s1, self.s2, self.s3])

    async def test_aiterator(self):
        qs = SimpleModel.objects.aiterator()
        results = []
        async for m in qs:
            results.append(m)
        self.assertCountEqual(results, [self.s1, self.s2, self.s3])

    async def test_aiterator_prefetch_realted(self):
        qs = SimpleModel.objects.prefetch_related("relatedmodels").aiterator()
        msg = "Using QuerySet.aiterator() after prefetch_related() is not supported."
        with self.assertRaisesMessage(NotSupportedError, msg):
            async for m in qs:
                pass


