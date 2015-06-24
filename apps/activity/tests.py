from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.bio.factories import PersonFactory
from .models import HttpRequest


class ActivityBaseTestCase(TestCase):

    def setUp(self):
        HttpRequest.objects.all().delete()

    def test_generate_model_from_response(self):
        url = reverse('activity:list')
        self.client.get(url)
        # check if HttpRequest model is created
        self.assertEqual(len(HttpRequest.objects.all()), 1)

    def test_generate_model_from_404_response(self):
        response = self.client.get('/some_nonsense_url')
        # check if HttpRequest model is created
        if response.status_code == 404:
            self.assertEqual(HttpRequest.objects.last().status_code, 404)

    def test_template(self):
        url = reverse('activity:list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'activity/list.html')

    def test_view(self):
        url = reverse('activity:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_request_priority(self):
        # create person for page rendering
        PersonFactory().save()
        # generate 3x http requests
        url = reverse('bio:single')
        self.client.get(url)
        url = reverse('activity:list')
        self.client.get(url)
        url = reverse('bio:edit')
        self.client.get(url)
        # give the middle one the biggest priority
        httpreq = HttpRequest.objects.all()[1]
        httpreq.priority = 199
        httpreq.save()
        # check if element sorted by prioryty
        self.assertEqual(HttpRequest.objects.first().priority,
                         httpreq.priority)
