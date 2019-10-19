from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
"""
# CMPE 272
# Group: Blue Hats
"""

class tweets(models.Model):
    tweet_message = models.CharField(max_length=400)
    tweet_id = models.CharField(max_length=50)
    screen_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tweet_message

    def get_post_url(self):
        return reverse('post_tweet', kwargs={'pk': self.pk})