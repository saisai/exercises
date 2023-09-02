from django.db import models

# Create your models here.
'''
import re
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

class Hand:
    """A hand of cards (bridge style)"""

    def __init__(self, north, east, south, west):
        # Input parameters are lists of cards ('Ah', '9s', etc.)
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    # ... (other possibly useful methods omitted) ...

def parse_hand(hand_string):
    """Takes a string of cards and splits into a full hand."""
    #p1 = re.compile('.{26}')
    p1 = re.compile('.{1}')
    #p2 = re.compile('..')
    p2 = re.compile('.')
    args = [p2.findall(x) for x in p1.findall(hand_string)]
    if len(args) != 4:
        raise ValidationError(_("Invalid input for a Hand instance"))
    return Hand(*args)


class HandField(models.Field):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        self.max_length = kwargs['max_length']
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        print('from_db_value ', value)
        if value is None:
            return value
        return parse_hand(value)

    def to_python(self, value):
        print('to_python ', value)
        if isinstance(value, Hand):
            return value

        if value is None:
            return value

        return parse_hand(value)

    def get_internal_type(self):
        return 'CharField'

    def db_type(self, connection):
        return 'CharField'

    def get_prep_value(self, value):
        return ''.join([''.join(l) for l in (value.north,
                                             value.east, value.south, value.west)])

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs


'''

from django.db import models
from django.db.models import BinaryField
import re
from django.core.exceptions import ValidationError


class Hand(object):
    """A hand of cards (bridge style)"""

    def __init__(self, north, east, south, west):
        # Input parameters are lists of cards ('Ah', '9s', etc)
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def parse_hand(hand_string):
    """Takes a string of cards and splits into a full hand."""
    p1 = re.compile('.{26}')
    p2 = re.compile('..')
    args = [p2.findall(x) for x in p1.findall(hand_string)]
    if len(args) != 4:
        raise ValidationError("Invalid input for a Hand instance")
    return Hand(*args)


class HandField(models.Field):
    description = 'A hand of cards (bridge style)'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super(HandField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(HandField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context=None):
        if value is None:
            return value
        return parse_hand(value)

    def to_python(self, value):
        if isinstance(value, Hand):
            return value
        if value is None:
            return value
        return parse_hand(value)

    def get_prep_value(self, value):
        '''将python对象转回查询值'''
        return ''.join([''.join(l) for l in (value.north,
                                             value.east, value.south, value.west)])
    '''
    removed-features-1-10
    https://docs.djangoproject.com/en/3.2/releases/1.10/#removed-features-1-10
    def get_prep_lookup(self, lookup_type, value):
        # We only handle 'exact' and 'in'. All others are errors.
        if lookup_type == 'exact':
            return self.get_prep_value(value)
        elif lookup_type == 'in':
            return [self.get_prep_value(v) for v in value]
        else:
            raise TypeError('Lookup type %r not supported.' % lookup_type)
    '''
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'max_length': self.max_length}
        defaults.update(kwargs)
        return super(HandField, self).formfield(**defaults)

    def get_internal_type(self):
        return 'CharField'

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    # https://my.oschina.net/acutesun/blog/1518417

class HelloCustom(models.Model):
    hand = HandField(max_length=104)

from django.db.models.lookups import Exact

class MyFieldExact(Exact):
    def as_sql(self, compiler, connection):
        # Avoid comparison against direct rhs if lhs is a boolean value. That
        # turns "boolfield__exact=True" into "WHERE boolean_field" instead of
        # "WHERE boolean_field = True" when allowed.
        if (
            isinstance(self.rhs, bool) and
            getattr(self.lhs, 'conditional', False) and
            connection.ops.conditional_expression_supported_in_where_clause(self.lhs)
        ):
            lhs_sql, params = self.process_lhs(compiler, connection)
            template = '%s' if self.rhs else 'NOT %s'
            return template % lhs_sql, params
        return super().as_sql(compiler, connection)

HandField.register_lookup(MyFieldExact)