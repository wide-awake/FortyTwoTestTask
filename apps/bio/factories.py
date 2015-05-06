from datetime import date

import factory
from django.contrib.webdesign import lorem_ipsum

from .models import Person


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person

    @factory.lazy_attribute
    def first_name(self):
        return lorem_ipsum.words(1, False).capitalize()

    @factory.lazy_attribute
    def last_name(self):
        return lorem_ipsum.words(1, False).capitalize()

    @factory.lazy_attribute
    def date_of_birth(self):
        return date.today()

    @factory.lazy_attribute
    def bio(self):
        return lorem_ipsum.sentence()

    @factory.lazy_attribute
    def email(self):
        return '{}_{}@example.com'.format(self.first_name.lower(), self.last_name.lower())

    @factory.lazy_attribute
    def jabber(self):
        return self.email

    @factory.lazy_attribute
    def skype(self):
        return '{}_{}'.format(self.first_name.lower(), self.last_name.lower())

    @factory.lazy_attribute
    def other(self):
        return lorem_ipsum.sentence()