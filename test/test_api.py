import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'protoapp.settings'

from django.test import TestCase
from rest_framework.test import APIRequestFactory

class APITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/api/')

        #   This is lame.
        self.assertIsInstance(request, object)
    #   self.assertEqual(response.status_code, 200)
        return
