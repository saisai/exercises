"""
learn
import arrow
from django.utils import timezone

from rest_framework.serializers import Field


class DateTimeField(Field):

    def to_representation(self, value):
        if not value:
            return 0
        formatted_value = arrow.Arrow.fromdatetime(value, tzinfo=timezone.get_current_timezone())
        return formatted_value.timestamp

    def to_internal_value(self, data):
        value = arrow.get(data).to(tz=timezone.get_current_timezone())
        return datetime.datetime.strptime(value.format("YYYYMMDDHHmmss"), "%Y%m%d%H%M%S")


class DateField(Field):

    def to_representation(self, value):
        if not value:
            return 0
        formatted_value = arrow.Arrow.fromdate(value, tzinfo=timezone.get_current_timezone())
        return formatted_value.timestamp

    def to_internal_value(self, data):
        value = arrow.get(data).to(tz=timezone.get_current_timezone())
        return datetime.datetime.strptime(value.format("YYYYMMDD"), "%Y%m%d")
        
from rest_framework import serializers

class AppAuthTokenSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(AppAuthTokenSerializer, self).__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)
        
https://www.youtube.com/watch?v=D_JYjEBedk4&list=PLFD1020FE0CB288FC&ab_channel=jakobsg1
"""

def format_date(cur_date):
    return cur_date.strftime('%Y-%m-%d')


def date_period(category, now):
    if category in (2,):
        '''
        Today
        '''
        return today_period(now)
    elif category in (3,):
        '''
        Yesterday
        '''
        return yesterday_period(now)
    elif category in (4,):
        '''
        This Week
        '''
        return this_week_period(now)
    elif category in (5,):
        '''
        Last Week
        '''
        return last_week_period(now)
    elif category in (6,):
        '''
        This Month
        '''
        return this_month_period(now)
    elif category in (7,):
        '''
        Last Month
        '''
        return last_month_period(now)


def today_period(now):
    start = now
    end = now + datetime.timedelta(days=1)
    return start, end


def yesterday_period(now):
    start = now + datetime.timedelta(days=-1)
    end = now
    return start, end


def this_week_period(now):
    index = WEEKDAY_LIST.index(now.weekday())
    start = now + datetime.timedelta(days=-index)
    end = now + datetime.timedelta(days=1)
    return start, end


def last_week_period(now):
    index = WEEKDAY_LIST.index(now.weekday())
    start = now + datetime.timedelta(days=-(7 + index))
    end = now + datetime.timedelta(days=-index)
    return start, end


def this_month_period(now):
    start = now + datetime.timedelta(days=-(now.day - 1))
    end = now + datetime.timedelta(days=1)
    return start, end


def last_month_period(now):
    last_end = now + datetime.timedelta(days=-now.day)
    start = last_end + datetime.timedelta(days=-(last_end.day - 1))
    end = last_end + datetime.timedelta(days=1)
    return start, end
	
def datetime_format(val):
    """
    Format val to %Y%m%d%H%M%S
    App will use same format to reserve the value
    :param val:
    :return:
    """
    if not val:
        return ""
    time_str = val.strftime('%Y%m%d%H%M%S')
    return time_str


def date_format(val):
    """
    Format val to %Y%m%d
    App will use same format to reserve the value
    :param val:
    :return:
    """
    if not val:
        return ""
    time_str = val.strftime('%Y%m%d')
    return time_str