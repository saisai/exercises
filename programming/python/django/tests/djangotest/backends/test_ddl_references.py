from django.db import connection
from django.db.backends.ddl_references import (
        Columns,
        Expressions,
        ForeignKeyName,
        IndexName,
        Statement,
        Table,
        )
from django.db.models import ExpressionList, F
from django.db.models.functions import Upper 
from django.db.models.indexes import IndexExpression
from django.db.models.sql import Query
from django.test import SimpleTestCase, TransactionTestCase 

from .models import Person 

class TableTests(SimpleTestCase):

    def setUp(self):
        self.reference = Table("table", lambda table: table.upper())


    def test_reference_table(self):
        self.assertIs(self.reference.references_table("table"), True)
        self.assertIs(self.reference.references_table("other"), False)

    def test_rename_table_references(self):
        self.reference.rename_table_references("other", "table")
        self.assertIs(self.reference.references_table("table"), True)
        self.assertIs(self.reference.references_table("other"), False)
        self.reference.rename_table_references("table", "other")
        self.assertIs(self.reference.references_table("table"), False)
        self.assertIs(self.reference.references_table("other"), True)

    def test_repr(self):
        self.assertEqual(repr(self.reference), "<Table 'TABLE'>")

    def test_str(self):
        self.assertEqual(str(self.reference), "TABLE")
