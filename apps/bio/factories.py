from datetime import date

import factory
from django.contrib.webdesign import lorem_ipsum

from .models import Person


class PersonFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Person

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

    @factory.lazy_attribute_sequence
    def email(self):
        return '{}_{}@example.com'.format(self.first_name, self.last_name)

    @factory.lazy_attribute_sequence
    def jabber(self):
        return self.email

    @factory.lazy_attribute_sequence
    def skype(self):
        return '{}_{}'.format(self.first_name, self.last_name)

    @factory.lazy_attribute_sequence
    def other(self):
        return lorem_ipsum.sentence()