from django.apps import apps
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.core.exceptions import FieldDoesNotExist
from django.db.models import CharField, Field, ForeignObjectRel, ManyToManyField
from django.db.models.options import EMPTY_RELATION_TREE, IMMUTABLE_WARNING
from django.test import SimpleTestCase

from .models import (
    AbstractPerson,
    BasePerson,
    Child,
    CommonAncestor,
    FirstParent,
    Person,
    ProxyPerson,
    Relating,
    Relation,
    SecondParent,
)
from .results import TEST_RESULTS

class OptionsBaseTests(SimpleTestCase):
    def _map_related_query_names(self, res):
        return tuple((o.name, m) for o, m in res)

    def _map_names(self, res):
        return tuple((f.name, m) for f, m in res)

    def _model(self, current_model, field):
        model = field.model._meta.concrete_model
        return None if model == current_model else model

    def _details(self, current_model, relation):
        direct = isinstance(relation, (Field, GenericForeignKey))
        model = relation.model._meta.concrete_model
        if model == current_model:
            model = None
        field = relation if direct else relation.field
        return (
                relation,
                model,
                direct,
                bool(field.many_to_many),
                )   # many_to_many can be None

class GetFieldsTests(OptionsBaseTests):
    def test_get_fields_is_immutable(self):
        msg = IMMUTABLE_WARNING % "get_fields()"
        print(Person._meta.get_fields())

        for _ in range(2):
            # Running unit test twice to ensure both non-cached and cached result
            # are immutable.
            fields = Person._meta.get_fields()
            with self.assertRaisesMessage(AttributeError, msg):
                fields += ["errors"]
                    
