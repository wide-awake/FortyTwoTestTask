from __future__ import print_function
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.forms.models import model_to_dict
from django.http import HttpResponse

from django.conf import settings

from .models import Person
from .forms import PersonForm


def single(request, **kwargs):
    p = Person.objects.all()[0]
    print("kwargs: ", kwargs)
    return render_to_response('bio/person.html', {'object': p})


def ajax_update(request):
    p = Person.objects.all()[0]
    if request.POST:
        import time
        time.sleep(3)
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
    success_url = reverse_lazy("bio:single")

