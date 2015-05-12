from django.test import TestCase
from django.core.urlresolvers import reverse

from .factories import PersonFactory
from .models import Person


class BioTestCase(TestCase):

    def setUp(self):
        Person.objects.all().delete()

    def test_person_context_and_template(self):
        p = PersonFactory()
        p.save()
        url = reverse('bio:single')
        response = self.client.get(url)
        person_context = response.context['object']
        # check page status code
        self.assertEqual(response.status_code, 200)
        # check we've used the right template
        self.assertTemplateUsed(response, 'bio/person.html')
        # check if person data in context
        self.assertEqual(p, person_context)