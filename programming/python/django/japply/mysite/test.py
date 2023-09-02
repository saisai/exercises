#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json

#sys.path.insert(0, "/d/exercises/python/django/japply/mysite/")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

#print(sys.path)
from jobsdb.models import Jobs_db

#data = [f.strip() for f in open('download.json', encoding="utf-8")]

f = open('download.json', encoding="utf-8")


if Jobs_db.objects.count() < 0:
    data = json.load(f)
    for obj in data['jobsdb']:
        Jobs_db.objects.create(
            title=obj['title'],
            link =obj['link']        
        )
    #print(obj['title'], obj['link'])

#for f in data:
#    print(f + "adadf")



#obj = Jobs_db.objects.all()

#print(obj.count())
