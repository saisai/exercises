from django.contrib import admin

# Register your models here.

from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    
admin.site.register(Subject, SubjectAdmin)

