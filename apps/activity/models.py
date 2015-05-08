from django.db import models


class HttpRequest(models.Model):
    date = models.DateTimeField("Request time", auto_now=True, auto_now_add=True)
    method = models.CharField("Request method", max_length=16)
    server_protocol = models.CharField(max_length=16)
    status_code = models.IntegerField()
    url = models.CharField("Request url", max_length=255)
    content_len = models.IntegerField()

    def __str__(self):
        return "[{}] at {} for {}".format(self.method, self.date, self.url)

    class Meta:
        ordering = ['-date']

