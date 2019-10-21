import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
import unittest
from assertpy import assert_that
from ..views import getAPIAuth, post_create, post_list, post_delete


# initialize the APIClient app
client = Client()

# to check authentication
class BasicTests(unittest.TestCase):
    def test_request_response(self):
        response = getAPIAuth()
        # Assert that the request-response cycle completed successfully with status code 200.
        print("unit test 1", response)
        self.assertEqual(response.status_code, 200)
        assert_that(response.ok, "Http request ok").is_true()

    def test_create_tweet_api(self):
        api = getAPIAuth()
        tweets = api.GetUserTimeline(screen_name='invalid_name') # with non existing user
        print("unit test 2")
        self.assertEqual(tweets.status_code, 826)
        self.assertEqual(tweets.status_code, 914)


if __name__ == "__main__":
    unittest.main()