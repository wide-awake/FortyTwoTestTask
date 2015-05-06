#!/usr/bin/python3
from apps.bio.factories import PersonFactory

# load single person in database
p = PersonFactory()
p.save()