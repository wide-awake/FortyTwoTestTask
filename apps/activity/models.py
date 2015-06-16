from django.db import models

from swampdragon.models import SelfPublishModel
from .serializers import HttpRequestSerializer


class HttpRequest(SelfPublishModel, models.Model):
    serializer_class = HttpRequestSerializer

    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField("Request method", max_length=16)
    server_protocol = models.CharField(max_length=16)
    status_code = models.IntegerField()
    url = models.CharField("Request url", max_length=255)
    content_len = models.IntegerField()
    priority = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return "[{}] at {} for {}".format(self.method, self.date, self.url)

    @property
    def overall(self):
        return len(HttpRequest.objects.all())

    @property
    def date_formated(self):
        return self.date.strftime("%c")

    class Meta:
        ordering = ['-priority']
