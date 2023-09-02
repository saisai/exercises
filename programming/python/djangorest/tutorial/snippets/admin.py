from django.contrib import admin

# Register your models here.

from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'linenos',  'code_language')
    list_display_links = ('title', 'code_language')
    list_editable = ('code',)
    list_filter = ('code',)
    ordering = ('title', 'code', 'linenos', )

    def code_language(self, obj):
        return obj.language + "->" + obj.code

    code_language.short_description = "Code Language"

admin.site.register(Snippet, SnippetAdmin)
