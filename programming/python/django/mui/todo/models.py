import datetime 

from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    end_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)