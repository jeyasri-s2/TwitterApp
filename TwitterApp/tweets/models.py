from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
"""
Author  : Jeyasri Subramanian
Date: October 10, 2019
"""

class tweets(models.Model):
    message = models.CharField(max_length=400)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_tweet', kwargs={'pk': self.pk})