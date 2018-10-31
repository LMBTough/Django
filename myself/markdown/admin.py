from django.contrib import admin
from .models import *


# Register your models here.

class MarkdownAdmin(admin.ModelAdmin):
    list_display = ('name', 'belong', 'check_day')
    list_display_links = ('name',)
    list_filter = ('check_day',)


class MindnodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'check_day')
    list_display_links = ('name',)
    list_filter = ('check_day',)


admin.site.register(Mindnode, MindnodeAdmin)
admin.site.register(Markdown, MarkdownAdmin)


# admin.site.register(Mindnode)
# admin.site.register(Markdown)
