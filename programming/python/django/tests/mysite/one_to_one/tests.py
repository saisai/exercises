from django.test import TestCase

# Create your tests here.
from django.db import IntegrityError, connection, transaction
from django.test import TestCase

from .models import (
    Bar,
    Director,
    Favorites,
    HiddenPointer,
    ManualPrimaryKey,
    MultiModel,
    Place,
    Pointer,
    RelatedModel,
    Restaurant,
    School,
    Target,
    ToFieldPointer,
    UndergroundBar,
    Waiter,
)


class OneToOneTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.p1 = Place.objects.create(name="Demon Dogs", address="944 W. Fullerton")
        cls.p2 = Place.objects.create(name="Ace Hardware", address="1013 N. Ashland")
        cls.r1 = Restaurant.objects.create(
            place=cls.p1, serves_hot_dogs=True, serves_pizza=False
        )
        cls.b1 = Bar.objects.create(place=cls.p1, serves_cocktails=False)

    def test_getter(self):
        # A Restaurant can access its place.
        self.assertEqual(repr(self.r1.place), "<Place: Demon Dogs the place>")
        # A Place can access its restaurant, if available.
        self.assertEqual(
            repr(self.p1.restaurant), "<Restaurant: Demon Dogs the restaurant>"
        )
        # p2 doesn't have an associated restaurant.
        with self.assertRaisesMessage(
            Restaurant.DoesNotExist, "Place has no restaurant"
        ):
            self.p2.restaurant
        # The exception raised on attribute access when a related object
        # doesn't exist should be an instance of a subclass of `AttributeError`
        # refs #21563
        self.assertFalse(hasattr(self.p2, "restaurant"))