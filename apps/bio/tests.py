from django.test import TestCase
from django.core.urlresolvers import reverse

from .factories import PersonFactory
from .models import Person


class BioBaseTestCase(TestCase):

    def setUp(self):
        Person.objects.all().delete()

    def test_person_context(self):
        p = PersonFactory()
        p.save()
        url = reverse('bio:single')
        response = self.client.get(url)
        person_context = response.context['object']
        # check if person data in context
        self.assertEqual(p, person_context)

    def test_template(self):
        p = PersonFactory()
        p.save()
        url = reverse('bio:single')
        response = self.client.get(url)
        # check we've used the right template
        self.assertTemplateUsed(response, 'bio/person.html')

    def test_view(self):
        p = PersonFactory()
        p.save()
        url = reverse('bio:single')
        response = self.client.get(url)
        # check page status code
        self.assertEqual(response.status_code, 200)


class BioFormTestCase(TestCase):

    def setUp(self):
        pass

    def test_math(self):
        # check if math still works :)
        self.assertEqual(2+2, 4)
