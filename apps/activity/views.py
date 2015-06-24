from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import HttpRequest


class HttpRequestList(ListView):
    model = HttpRequest
    paginate_by = 25
    template_name = "activity/list.html"


def ajax_polling(request):
    elements_so_far = request.GET['elements_so_far']
    try:
        new_elements = HttpRequest.objects.all().\
            order_by('priority', 'date')[elements_so_far:]
        return render_to_response(
            "activity/single.html", {'new_elements': new_elements})
    except IndexError:
        return HttpResponse(status=200)
