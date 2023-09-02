from django.contrib import admin

# Register your models here.

from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    
admin.site.register(ToDo, ToDoAdmin)