from datetime import date

from django.test import TestCase
from django.core.urlresolvers import reverse

from .factories import PersonFactory
from .models import Person


class BioTestCase(TestCase):

    def setUp(self):
        pass

    def test_page_status(self):
        url = reverse('bio:single')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)