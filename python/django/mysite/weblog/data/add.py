import re

import os
import django

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.mysite.settings")
#django.setup()

from mysite.weblog.models import Blog

data = [re.split(':' ,f.strip()) for f in open('readme.txt')]

for f in data:
    print(f)