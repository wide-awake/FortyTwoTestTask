import StringIO
from PIL import Image as Img

from django.db import models
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
    photo = models.ImageField(upload_to='/', null=True)

    def save(self, *args, **kwargs):
        if self.photo:
            image = Img.open(StringIO.StringIO(self.photo.read()))
            image.thumbnail((200, 200), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.photo = InMemoryUploadedFile(output, 'ImageField', self.photo.name, 'image/jpeg', output.len, None)
        # replace image instead
        try:
            current = Person.objects.get(id=self.id)
            if current.photo != self.photo:
                current.photo.delete(save=False)
        except:
            pass

        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class ChangeLog(models.Model):
    model_name = models.CharField(max_length=128)
    action = models.CharField(max_length=16)

    def __str__(self):
        return "{} on {}".format(self.action, self.model_name)