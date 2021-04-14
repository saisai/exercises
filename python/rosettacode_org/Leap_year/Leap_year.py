import calendar
print(calendar.isleap(2020))
print(calendar.isleap(2021))


def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


print(is_leap_year(2020))
print(is_leap_year(2021))

import datetime
def is_leap_year_2(year):
    try:
        datetime.date(year, 2, 29)
    except ValueError:
        return False
    return True

print(is_leap_year_2(2020))
print(is_leap_year_2(2021))
