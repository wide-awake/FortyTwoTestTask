from django.views.generic import ListView

from .models import HttpRequest


class HttpRequestList(ListView):
    model = HttpRequest
    paginate_by = 10
    template_name = "activity/list.html"
