import re

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from weblog.models import Blog, Author

def add_weblog():
    data = [re.split(':' ,f.strip()) for f in open('weblog/data/readme.txt')]

    for f in data:
        #print(f[0].strip(), f[1].strip())
        Blog.objects.create(name=f[0].strip(), tagline=f[1].strip())


def add_author():
    #data = [re.split(':', f.strip()) for f in open('weblog/data/authors.txt', encoding='utf-8')]
    data = [re.split(':', f.strip()) for f in open('weblog/data/authors2.txt', encoding='utf-8')]

    for f in data:
        # print(f[0].strip(), f[1].strip())
        #print(f[0].strip())
        Author.objects.create(name=f[0].strip())

add_author()