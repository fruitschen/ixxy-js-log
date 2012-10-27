from django.contrib import admin

from js_log.models import  Error

class ErrorOptions(admin.ModelAdmin):
    list_display = ['last_happened', 'number', 'short_message', 'user_agent']
    list_filter = ['last_happened', 'first_happened', 'short_message','user_agent']

admin.site.register(Error, ErrorOptions)
