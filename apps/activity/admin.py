from django.contrib import admin
from .models import HttpRequest

class HttpRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(HttpRequest, HttpRequestAdmin)