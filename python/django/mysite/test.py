import re

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from weblog.models import Blog


data = [re.split(':' ,f.strip()) for f in open('weblog/data/readme.txt')]

for f in data:
    #print(f[0].strip(), f[1].strip())
    Blog.objects.create(name=f[0].strip(), tagline=f[1].strip())


