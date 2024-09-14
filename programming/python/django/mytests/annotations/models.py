
from django.db import models

class Branch(models.Model):

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

class Student(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    branch = models.ManyToManyField(Branch)



