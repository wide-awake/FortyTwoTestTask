#!/usr/bin/python3
from django.contrib.auth.models import User
from apps.bio.factories import PersonFactory


# load single person in database
PersonFactory().save()

# creating superuser
login = 'admin'
password = login
User.objects.create_superuser(login, 'e@e.com', password).save()
print("Firxtures loaded!")
print("Admin user login/password: {}/{}".format(login, password))
