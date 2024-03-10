import datetime
import pickle
import unittest
import uuid
from collections import namedtuple
from copy import deepcopy
from decimal import Decimal
from unittest import mock
import os 

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest.settings")
django.setup()

from django.core.exceptions import FieldError
from django.db import DatabaseError, NotSupportedError, connection
from django.db.models import (
    AutoField,
    Avg,
    BinaryField,
    BooleanField,
    Case,
    CharField,
    Count,
    DateField,
    DateTimeField,
    DecimalField,
    DurationField,
    Exists,
    Expression,
    ExpressionList,
    ExpressionWrapper,
    F,
    FloatField,
    Func,
    IntegerField,
    Max,
    Min,
    Model,
    OrderBy,
    OuterRef,
    PositiveIntegerField,
    Q,
    StdDev,
    Subquery,
    Sum,
    TimeField,
    UUIDField,
    Value,
    Variance,
    When,
)
from django.db.models.expressions import (
    Col,
    Combinable,
    CombinedExpression,
    NegatedExpression,
    RawSQL,
    Ref,
)
from django.db.models.functions import (
    Coalesce,
    Concat,
    Left,
    Length,
    Lower,
    Substr,
    Upper,
)
from django.db.models.sql import constants
from django.db.models.sql.datastructures import Join
from django.test import SimpleTestCase, TestCase, skipUnlessDBFeature
from django.test.utils import (
    Approximate,
    CaptureQueriesContext,
    isolate_apps,
    register_lookup,
)
from django.utils.functional import SimpleLazyObject

from expressions.models import (
    UUID,
    UUIDPK,
    Company,
    Employee,
    Experiment,
    Manager,
    Number,
    RemoteEmployee,
    Result,
    SimulationRun,
    Time,
)

sql = Company.objects.all()

if sql.count() <= 0:
    example_inc = Company.objects.create(
            name="Example Inc.",
            num_employees=2300,
            num_chairs=5,
            ceo=Employee.objects.create(firstname="Joe", lastname="Smith", salary=10),
        )
    foobar_ltd = Company.objects.create(
            name="Foobar Ltd.",
            num_employees=3,
            num_chairs=4,
            based_in_eu=True,
            ceo=Employee.objects.create(firstname="Frank", lastname="Meyer", salary=20),
        )
    max = Employee.objects.create(
            firstname="Max", lastname="Mustermann", salary=30
        )
    gmbh = Company.objects.create(
            name="Test GmbH", num_employees=32, num_chairs=1, ceo=max
        )

companies = (
            Company.objects.annotate(
                salaries=F("ceo__salary"),
            )
            .values("num_employees", "salaries")
            .aggregate(
                result=Sum(
                    F("salaries") + F("num_employees"), output_field=IntegerField()
                ),
            )
        )
        
print(companies)
