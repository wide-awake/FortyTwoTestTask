import StringIO
from PIL import Image as Img

from django.db import models
from django.utils.html import mark_safe
from django.core.files.uploadedfile import InMemoryUploadedFile


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField(max_length=255)
    jabber = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    other = models.TextField()
    photo = models.ImageField(upload_to='photo/', null=True)

    def save(self, *args, **kwargs):
        if self.photo:
            image = Img.open(StringIO.StringIO(self.photo.read()))
            image.thumbnail((200, 200), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.photo = InMemoryUploadedFile(output, 'ImageField',
                                              self.photo.name, 'image/jpeg',
                                              output.len, None)
        # replace image instead
        try:
            current = Person.objects.get(id=self.id)
            if current.photo != self.photo:
                current.photo.delete(save=False)
        except:
            pass

        super(Person, self).save(*args, **kwargs)

    def admin_image(self):
        if self.photo:
            return mark_safe('<img src="%s" width="75px"/>' % self.photo.url)
        else:
            return '<no phoro>'

    admin_image.short_description = "Photo Preview"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class ChangeLog(models.Model):
    model_name = models.CharField(max_length=128)
    action = models.CharField(max_length=16)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return "{} on {}".format(self.action, self.model_name)
