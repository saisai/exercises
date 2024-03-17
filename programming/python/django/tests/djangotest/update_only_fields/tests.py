from django.db.models.signals import post_save, pre_save 
from django.test import TestCase


from .models import  Account, Employee, Person, Profile, ProxyEmployee 


class UpdateOnlyFieldsTests(TestCase):
    msg = (
             "The following fields do not exist in this model, are m2m fields, or "
            "are non-concrete fields: %s"
            )
    def test_update_fields_basic(self):
        s = Person.objects.create(name="Sara", gender="F")
        self.assertEqual(s.gender, "F")


        s.gender = "M"
        s.name = "Ian"
        s.save(update_fields=['name'])

        s = Person.objects.get(pk=s.pk)
        print(s.gender)
        print(s.name)

        self.assertEqual(s.gender, "F")
        self.assertEqual(s.name, "Ian")

    def test_update_fields_deferred(self):
        s = Person.objects.create(name="Sara", gender="F", pid=22)
        self.assertEqual(s.gender, "F")

        s1 = Person.objects.defer("gender", "pid").get(pk=s.pk)
        s1.name = "Emily"
        s1.gender = "M"


        with self.assertNumQueries(1):
            s1.save()

        s2 = Person.objects.get(pk=s1.pk)
        self.assertEqual(s2.name, "Emily")
        self.assertEqual(s2.gender, "M")

    def test_update_fields_only_2(self):
        s = Person.objects.create(name="Sara", gender="F", pid=22)
        self.assertEqual(s.gender, "F")

        s1 = Person.objects.only("name").get(pk=s.pk)
        s1.name = "Emily"
        s1.gender = "M"

        with self.assertNumQueries(2):
            s1.save(update_fields=["pid"])

        s2 = Person.objects.get(pk=s1.pk)
        self.assertEqual(s2.name, "Sara")
        self.assertEqual(s2.gender, "F")
