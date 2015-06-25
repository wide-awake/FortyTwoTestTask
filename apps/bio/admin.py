from django.contrib import admin
from .models import Person, ChangeLog


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email',
                    'jabber', 'skype', 'admin_image')
    # readonly_fields = ('admin_image',)


class ChangeLogAdmin(admin.ModelAdmin):
    pass
    # list_filter = ('',)


admin.site.register(Person, PersonAdmin)
admin.site.register(ChangeLog, ChangeLogAdmin)
