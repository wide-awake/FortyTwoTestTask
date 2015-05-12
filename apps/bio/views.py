from django.shortcuts import render_to_response

from .models import Person


def single(request):
    p = Person.objects.all()[0]
    return render_to_response('bio/person.html', {'object': p})