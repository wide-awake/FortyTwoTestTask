from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField(max_length=255)
    jabber = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    other = models.TextField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
