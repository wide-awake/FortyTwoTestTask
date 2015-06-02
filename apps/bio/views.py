from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.forms.models import model_to_dict
from django.http import HttpResponse

from django.conf import settings

from .models import Person
from .forms import PersonForm


def single(request):
    p = Person.objects.all()[0]
    return render_to_response('bio/person.html', {'object': p})


def ajax_update(request):
    # TODO: remove this in production
    if settings.DEBUG:
        import time
        time.sleep(2)

    instance = Person.objects.all()[0]
    try:
        for attr, value in request.POST.iteritems():
            setattr(instance, attr, value)
        instance.save()
    except IndexError:
        return HttpResponse(status=400)

    return HttpResponse(status=200)


class PersonEdit(FormView):

    def __init__(self, *args, **kwargs):
        super(PersonEdit, self).__init__(*args, **kwargs)
        self.initial = model_to_dict(Person.objects.first())

    form_class = PersonForm
    template_name = 'bio/edit.html'
    success_url = reverse_lazy("bio:single")

