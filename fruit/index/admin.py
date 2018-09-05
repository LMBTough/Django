from django.contrib import admin
from .models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']
    list_editable = ['age']
    list_filter = ['age']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_editable = ['address']
    list_display_links = ['name']
    list_filter = ['address']
    fieldsets = (
        ('基本选项', {'fields': ['name', 'address']}),
        ('高级选项', {'fields': ['website'], 'classes': ('collapse',)})
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Wife)
