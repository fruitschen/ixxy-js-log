from django.contrib import admin

from js_log.models import  Error

class ErrorOptions(admin.ModelAdmin):
    list_display = ['last_happened', 'number', ]
    list_filter = ['last_happened', 'first_happened']

admin.site.register(Error, ErrorOptions)
