from __future__ import print_function
from django.shortcuts import render_to_response
from django.views.generic import FormView
from django.forms.models import model_to_dict
from django.http import HttpResponse

from .models import Person
from .forms import PersonForm
from .filelogger import model_log, req_log


def single(request):
    p = Person.objects.all()[0]
    model_log(p)
    req_log(request)
    return render_to_response('bio/person.html', {'object': p})


def ajax_update(request):
    p = Person.objects.all()[0]
    model_log(p)
    req_log(request)
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
