import StringIO
from PIL import Image as Img

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

from utils.generate_upload_name import generate_upload_name


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField(max_length=255)
    jabber = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    other = models.TextField()
    photo = models.ImageField(upload_to='%Y/%m/%d', null=True)

    def save(self, *args, **kwargs):
        if self.photo:
            image = Img.open(StringIO.StringIO(self.photo.read()))
            image.thumbnail((200,200), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.photo = InMemoryUploadedFile(output, 'ImageField', "%s" % self.photo.name, 'image/jpeg', output.len, None)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)