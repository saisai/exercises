from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class QuestionAdmins(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


class QuestionAdmin2(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
