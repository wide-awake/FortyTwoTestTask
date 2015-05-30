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


class PersonFormTestCase(TestCase):

    def setUp(self):
        Person.objects.all().delete()
        self.p = PersonFactory()
        self.p.save()

    def test_form(self):
        update_url = reverse('bio:edit')
        r = self.client.get(update_url)
        data = r.context['form'].initial
        # generate new data
        new_data = PersonFactory()
        # update some data
        data['first_name'] = new_data.first_name
        data['last_name'] = new_data.last_name
        data['date_of_birth'] = new_data.date_of_birth
        data['bio'] = new_data.bio
        data['email'] = new_data.email
        data['jabber'] = new_data.jabber
        data['skype'] = new_data.skype
        data['other'] = new_data.other
        # post to the form
        r = self.client.post(update_url, data)
        # retrieve again
        r = self.client.get(update_url)
        # self.assertContains(r, 'updated_value')
        self.assertEqual(r.context['form'].initial['first_name'], new_data.first_name)
        self.assertEqual(r.context['form'].initial['last_name'], new_data.last_name)
        self.assertEqual(r.context['form'].initial['date_of_birth'], new_data.date_of_birth)
        self.assertEqual(r.context['form'].initial['bio'], new_data.bio)
        self.assertEqual(r.context['form'].initial['email'], new_data.email)
        self.assertEqual(r.context['form'].initial['jabber'], new_data.jabber)
        self.assertEqual(r.context['form'].initial['skype'], new_data.skype)
        self.assertEqual(r.context['form'].initial['other'], new_data.other)
