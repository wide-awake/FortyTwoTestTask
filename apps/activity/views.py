from django.views.generic import ListView
from django.conf import settings

from .models import HttpRequest


class HttpRequestList(ListView):
    model = HttpRequest
    paginate_by = settings.SWAMP_DRAGON['request_to_show']
    template_name = "activity/list.html"
