from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    
    
    class Meta:
        ordering = ('age', )
        app_label = 'student'
