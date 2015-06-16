from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .factories import PersonFactory
from .models import Person, ChangeLog


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
        PersonFactory().save()
        url = reverse('bio:single')
        response = self.client.get(url)
        # check we've used the right template
        self.assertTemplateUsed(response, 'bio/person.html')

    def test_view(self):
        PersonFactory().save()
        url = reverse('bio:single')
        response = self.client.get(url)
        # check page status code
        self.assertEqual(response.status_code, 200)


class PersonFormTestCase(TestCase):

    def setUp(self):
        # reload person bio
        Person.objects.all().delete()
        self.p = PersonFactory()
        self.p.save()
        # crete super user
        self.user = 'admin'
        self.password = self.user
        admin = User.objects.create_superuser(self.user, 'e@e.com', self.password)
        admin.save()

    def test_admin_login(self):
        self.assertEqual(Client().login(username=self.user, password=self.password), True)

    def test_form_saving(self):
        form_url = reverse('bio:edit')
        ajax_url = reverse('bio:ajax-update')
        # log in to acscess page
        c = Client()
        c.login(username=self.user, password=self.password)
        r = c.get(form_url)
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
        r = c.post(ajax_url, data)
        self.assertEqual(r.status_code, 200)
        # retrieve from DB abd check if data was saved
        instance = Person.objects.all()[0]
        self.assertEqual(instance.first_name, new_data.first_name)
        self.assertEqual(instance.last_name, new_data.last_name)
        self.assertEqual(instance.date_of_birth.strftime('%Y-%m-%d'), new_data.date_of_birth)
        self.assertEqual(instance.bio, new_data.bio)
        self.assertEqual(instance.email, new_data.email)
        self.assertEqual(instance.jabber, new_data.jabber)
        self.assertEqual(instance.skype, new_data.skype)
        self.assertEqual(instance.other, new_data.other)

    def test_form_page_status(self):
        c = Client()
        c.login(username=self.user, password=self.password)
        form_url = reverse('bio:edit')
        response = c.get(form_url)
        self.assertEqual(response.status_code, 200)


class TemplateTagsTestCase(TestCase):

    def setUp(self):
        Person.objects.all().delete()
        PersonFactory().save()

    def test_edit_link_templatetag(self):
        r = self.client.get(reverse('bio:single'))
        self.assertIn('admin/bio/person/1/', r.content)


class SignalTestCase(TestCase):
    def setUp(self):
        Person.objects.all().delete()
        PersonFactory().save()

    def test_signal_on_create(self):
        p = PersonFactory()
        count = ChangeLog.objects.all().count()
        p.save()
        new_count = ChangeLog.objects.all().count()
        self.assertEqual(count + 1, new_count)

    def test_signal_on_update(self):
        PersonFactory().save()
        p = Person.objects.first()
        count = ChangeLog.objects.all().count()
        p.first_name = 'Marshall Mathers'
        p.save()
        new_count = ChangeLog.objects.all().count()
        self.assertEqual(count + 1, new_count)

    def test_signal_on_delete(self):
        PersonFactory().save()
        p = Person.objects.first()
        count = ChangeLog.objects.all().count()
        p.delete()
        new_count = ChangeLog.objects.all().count()
        self.assertEqual(count + 1, new_count)
