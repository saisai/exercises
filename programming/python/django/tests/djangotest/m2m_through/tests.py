from datetime import date, datetime, timedelta
from operator import attrgetter

from django.db import IntegrityError
from django.test import TestCase

from .models import (
    CustomMembership,
    Employee,
    Event,
    Friendship,
    Group,
    Ingredient,
    Invitation,
    Membership,
    Person,
    PersonChild,
    PersonSelfRefM2M,
    Recipe,
    RecipeIngredient,
    Relationship,
    SymmetricalFriendship,
)


class M2mThroughTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.bob = Person.objects.create(name="Bob")
        cls.jim = Person.objects.create(name="Jim")
        cls.jane = Person.objects.create(name="Jane")
        cls.rock = Group.objects.create(name="Rock")
        cls.roll = Group.objects.create(name="Roll")

    def test_reverse_inherited_m2m_with_through_fields_list_hashable(self):
        reverse_m2m = Person._meta.get_field("events_invited")
        self.assertEqual(reverse_m2m.through_fields, ["event", "invitee"])
        inherited_reverse_m2m = PersonChild._meta.get_field("events_invited")
        self.assertEqual(inherited_reverse_m2m.through_fields, ["event", "invitee"])
        self.assertEqual(hash(reverse_m2m), hash(inherited_reverse_m2m))
