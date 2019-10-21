'''
Manmeet Singh
Oct 20, 2019
'''
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
import twitter

client=Client()
class YourTestClass(TestCase):
    @classmethod
    def setUp(self):
        api = twitter.Api(consumer_key='pM8VhaCuNyMr7tuPiJGSACyr0',
                        consumer_secret='H4D3NtRpSEXmR7aseowaoFedMLt1I7BEyUI5M20q7rH2kqM5hk',
                        access_token_key='1180201895551328257-OhsK5pMcFNxiyJWUlyCwfp6ArHc5Lj',
                        access_token_secret='rN8S32KUULpewDWmxvkrefG3r6JyeKuyoNbxWXIIEgAyZ')
        pass

    def test_get_home_page(self):
        response = client.get(reverse('tweets:post_list'))
        #print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BlueHatsSjsu")
        pass

    def test_post_new_tweet(self):
        response = client.post('/tweets/create', {'message': 'test tweet'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('tweets:post_list'))
        self.assertContains(response, "test tweet")
        pass
