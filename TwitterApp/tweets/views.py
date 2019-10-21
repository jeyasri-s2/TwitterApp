from __future__ import unicode_literals
import twitter
import json
"""
# CMPE 272
# Group: Blue Hats
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from tweets.models import tweets
from django.test import Client
# Create your views here.

def getAPIAuth():
    return twitter.Api(consumer_key='pM8VhaCuNyMr7tuPiJGSACyr0',
                      consumer_secret='H4D3NtRpSEXmR7aseowaoFedMLt1I7BEyUI5M20q7rH2kqM5hk',
                      access_token_key='1180201895551328257-OhsK5pMcFNxiyJWUlyCwfp6ArHc5Lj',
                      access_token_secret='rN8S32KUULpewDWmxvkrefG3r6JyeKuyoNbxWXIIEgAyZ')
api = getAPIAuth()

class PostsForm(ModelForm):
    class Meta:
        model = tweets
        fields = ['id', 'screen_name', 'tweet_message']


def post_list(request, template_name='tweets/post_list.html'):
    if (api != None):
        try:
            tweets = api.GetUserTimeline(screen_name='BlueHatsSjsu')
            print(tweets)
        except twitter.error.TwitterError as e:
            print(e)
            #[{'code': 50, 'message': 'User not found.'}]
    posts=[]
    for tweet in tweets:
        mytweet = {'text' : tweet.text, 'id': tweet.id_str, 'screenname': tweet.user.screen_name}
        posts.append(mytweet)
    #print(posts)

    return render(request, template_name, {'tweets': posts})
# Author: Manmeet and Subarna
def post_create(request, template_name='tweets/post_form.html'):
    form = PostsForm(request.POST or None)
    #print(form)
    #print(form.tweet_message)
    message = ''
    if form.is_valid():
        tweet_message = form.cleaned_data['tweet_message']
        if(api != None):
            try:
                api.PostUpdate(tweet_message)
                message = ''
                return redirect('tweets:post_list')
            except twitter.error.TwitterError as e:
                if(str(e.message).find('187')):
                    message = 'Duplicate tweet. Try new message !'

    #return redirect('tweets:post_list')
    return render(request, template_name, {'form': form, 'message': message})
# Author: Jeyasri
def post_update(request, pk, template_name='tweets/post_form.html'):
    post = get_object_or_404(tweets, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('tweets:post_list')
    return render(request, template_name, {'form': form})

# Author: Manmeet and Subarna
def post_delete(request, id, template_name='tweets/post_delete.html'):
    tweet = api.GetStatus(str(id))
    if request.method=='POST':
        api.DestroyStatus(str(id))
        return redirect('tweets:post_list')
    return render(request, template_name, {'object': tweet.text})
