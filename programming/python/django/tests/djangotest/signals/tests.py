from unittest import mock 

from asgiref.sync import markcoroutinefunction

from django import dispatch
from django.apps.registry import Apps
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.test import SimpleTestCase, TestCase 
from django.test.utils import isolate_apps 

from .models import Author, Book, Car, Page, Person


class BaseSignalSetup:
    def setUp(self):
        # Save up the number of connected signals so that we can check at the
        # end that all the signals we register get properly unregistered (#9989)
        self.pre_signals = (
                len(signals.pre_save.receivers),
                len(signals.post_save.receivers),
                len(signals.pre_delete.receivers),
                len(signals.post_delete.receivers),
                )

    def tearDown(self):
        # All our signals got disconnected properly
        post_signals = (
                len(signals.pre_save.receivers),
                len(signals.post_save.receivers),
                len(signals.pre_delete.receivers),
                len(signals.post_delete.receivers),
                )
        self.assertEqual(self.pre_signals, post_signals)





class SignalTests(BaseSignalSetup, TestCase):
    def test_model_Pre_init_and_post_init(self):
        data = []

        def pre_init_callback(sender, args, **kwargs):
            data.append(kwargs["kwargs"])

        signals.pre_init.connect(pre_init_callback)

        def post_init_callback(sender, instance, **kwargs):
            data.append(instance)

        signals.post_init.connect(post_init_callback)

        p1 = Person(first_name="John", last_name="Doe")
        self.assertEqual(data, [{}, p1])

    def test_save_signals(self):
        data = []

        def pre_save_handler(signal, sender, instance, **kwargs):
            data.append((instance, sender, kwargs.get("raw", False)))

        def post_save_handler(signal, sender, instance, **kwargs):
            data.append(
                    (instance, sender, kwargs.get("created"), kwargs.get("raw", False))
                    )

        signals.pre_save.connect(pre_save_handler, weak=False)
        signals.post_save.connect(post_save_handler, weak=False)

        try:
            p1 = Person.objects.create(first_name="John", last_name="Smith")

            self.assertEqual(
                data,
                [
                    (p1, Person, False),
                    (p1, Person, True, False),
                ],
            )
            data[:] = []

            p1.first_name = "Tom"
            p1.save()
            self.assertEqual(
                data,
                [
                    (p1, Person, False),
                    (p1, Person, False, False),
                ],
            )
            data[:] = []

            # Calling an internal method purely so that we can trigger a "raw" save.
            p1.save_base(raw=True)
            self.assertEqual(
                data,
                [
                    (p1, Person, True),
                    (p1, Person, False, True),
                ],
            )
            data[:] = []

            p2 = Person(first_name="James", last_name="Jones")
            p2.id = 99999
            p2.save()
            self.assertEqual(
                data,
                [
                    (p2, Person, False),
                    (p2, Person, True, False),
                ],
            )
            data[:] = []
            p2.id = 99998
            p2.save()
            self.assertEqual(
                data,
                [
                    (p2, Person, False),
                    (p2, Person, True, False),
                ],
            )

            # The sender should stay the same when using defer().
            data[:] = []
            p3 = Person.objects.defer("first_name").get(pk=p1.pk)
            p3.last_name = "Reese"
            p3.save()
            self.assertEqual(
                data,
                [
                    (p3, Person, False),
                    (p3, Person, False, False),
                ],
            )
        finally:
            signals.pre_save.disconnect(pre_save_handler)
            signals.post_save.disconnect(post_save_handler)
