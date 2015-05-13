from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory

from .models import HttpRequest
from .middlware import ReqCatchMiddleware
from .views import HttpRequestList


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


class HttpRequestMiddlwareTest(TestCase):
    def setUp(self):
        self.middlware = ReqCatchMiddleware()
        self.factory = RequestFactory()

    def test_model_data(self):
        url = reverse('activity:list')
        request = self.factory.get(url)
        # proceed middlware
        #self.middlware.process_response(request, response)
        # m = HttpRequest.objects.last()
        # self.assertEqual(self.request.status_code, m['status_code'])