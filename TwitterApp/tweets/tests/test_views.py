import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
import unittest
from ..views import getAPIAuth


# initialize the APIClient app
client = Client()

# to check authentication
class BasicTests(unittest.TestCase):
    def test_request_response(self):
        response = getAPIAuth()

        # Assert that the request-response cycle completed successfully with status code 200.
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()