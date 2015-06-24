from django.contrib import admin
from .models import Person, ChangeLog


class PersonAdmin(admin.ModelAdmin):
    pass


class ChangeLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(ChangeLog, ChangeLogAdmin)
