https://code.tutsplus.com/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
https://github.com/vubon/django-celery-redis
https://github.com/bharat1234567/Django-Celery-Tutorial
https://www.accordbox.com/blog/how-to-setup-celery-django/
https://testdriven.io/blog/django-and-celery/
https://github.com/AccordBox/awesome-scrapy

https://www.devart.com/odbc/mysql/docs/python.htm
https://algorithms.tutorialhorizon.com/dynamic-programming-longest-common-substring/

https://paddy3118.blogspot.com/2009/07/case-of-disappearing-over-bar.html

'''
  Reverse a Unicode string with proper handling of combining characters
'''

import unicodedata

def ureverse(ustring):
    '''
    Reverse a string including unicode combining characters

    Example:
        >>> ucode = ''.join( chr(int(n, 16))
                             for n in ['61', '73', '20dd', '64', '66', '305'] )
        >>> ucoderev = ureverse(ucode)
        >>> ['%x' % ord(char) for char in ucoderev]
        ['66', '305', '64', '73', '20dd', '61']
        >>> 
    '''
    groupedchars = []
    uchar = list(ustring)
    while uchar:
        if 'COMBINING' in unicodedata.name(uchar[0], ''):
            groupedchars[-1] += uchar.pop(0)
        else:
            groupedchars.append(uchar.pop(0))
    # Grouped reversal
    groupedchars = groupedchars[::-1]

    return ''.join(groupedchars)

if __name__ == '__main__':
    ucode = ''.join( chr(int(n, 16))
                     for n in ['61', '73', '20dd', '64', '66', '305'] )
    ucoderev = ureverse(ucode)
    print (ucode)
    print (ucoderev)
