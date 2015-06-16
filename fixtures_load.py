#!/usr/bin/python3
from django.contrib.auth.models import User
from apps.bio.factories import PersonFactory


# load single person in database
p = PersonFactory()
p.save()

# creating superuser
login = 'admin'
password = login
admin = User.objects.create_superuser(login, 'e@e.com', password)
admin.save()