"""
test_drf-dynamic-fields
-----------
Tests for `drf-dynamic-fields` mixins
"""

from collections import OrderedDict

from django.test import TestCase, RequestFactory

from .serializers import SchoolSerializer, TeacherSerializer
from .models import Teacher, School

class TestDynamicFieldsMixin(TestCase):
    """
    Test case for the DynamicFieldsMixin
    """

    def test_removes_fields(self):
        """
        Does it actually remove fields?
        """
        rf = RequestFactory()

        print(rf)
        request = rf.get("/api/v1/schools/1/?fields=id")
        print(request)
        serializer = TeacherSerializer(context={"request": request})

        print(serializer.data)
        self.assertEqual(set(serializer.fields.keys()), set(("id",)))
        print(serializer.fields)
        print(serializer.fields.keys())
    
