from __future__ import print_function
from datetime import datetime

from django.shortcuts import render_to_response
from django.views.generic import FormView
from django.http import HttpResponse
from django.forms.models import model_to_dict

from .models import Person
from .forms import PersonForm
from .filelogger import logger


def single(request):
    p = Person.objects.all()[0]
    logger.debug(model_to_dict(p))
    logger.info("[{}] path: {}, GET: {}, POST: {}".format(
        datetime.now(),
        request.path,
        request.GET,
        request.POST))
    return render_to_response('bio/person.html', {'object': p})


def ajax_update(request):
    p = Person.objects.all()[0]
    logger.debug(model_to_dict(p))
    logger.info("[{}] path: {}, GET: {}, POST: {}".format(
        datetime.now(),
        request.path,
        request.GET,
        request.POST))
    if request.POST:
        form = PersonForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)


class PersonEdit(FormView):

    def __init__(self, *args, **kwargs):
        super(PersonEdit, self).__init__(*args, **kwargs)
        self.initial = model_to_dict(Person.objects.first())

    form_class = PersonForm
    template_name = 'bio/edit.html'
