from __future__ import unicode_literals
import twitter
import json
"""
Author  : Jeyasri Subramanian
Date: October 10, 2019
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from tweets.models import tweets
# Create your views here.

class PostsForm(ModelForm):
    class Meta:
        model = tweets
        fields = ['id', 'screen_name', 'tweet_message']


def post_list(request, template_name='tweets/post_list.html'):
    api = getAPIAuth()
    if (api != None):
        try:
            tweets = api.GetUserTimeline(screen_name='BlueHatsSjsu')
            print(tweets)
        except twitter.error.TwitterError as e:
            print(e)
            #[{'code': 50, 'message': 'User not found.'}]


    posts = tweets.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name='tweets/post_form.html'):
    form = PostsForm(request.POST or None)
    #print(form)
    #print(form.tweet_message)
    message = ''
    if form.is_valid():
        tweet_message = form.cleaned_data['tweet_message']
        api = getAPIAuth()
        if(api != None):
            try:
                api.PostUpdate(tweet_message)
                message = ''
            except twitter.error.TwitterError as e:
                if(str(e.message).find('187')):
                    message = 'Duplicate tweet. Try new message !'

    return render(request, template_name, {'form': form, 'message': message})

def post_update(request, pk, template_name='tweets/post_form.html'):
    post = get_object_or_404(tweets, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('tweets:post_list')
    return render(request, template_name, {'form': form})

def post_delete(request, pk, template_name='tweets/post_delete.html'):
    post = get_object_or_404(tweets, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('tweets:post_list')
    return render(request, template_name, {'object': post})

def getAPIAuth():
    api = twitter.Api(consumer_key='YMicTnbDYP0nI4h4SZsFSlSJS',
                      consumer_secret='wJTgBYY1F6zqgLPJc01Id35ODTn29C7PjXln5KRhQo6c5gEXdM',
                      access_token_key='1182848959628185600-tGJqZie3sGqTZMAM8Zay69yncl6BMx',
                      access_token_secret='h1TEiYq2RziqHhKh5pS1jxRgshAWygxVoqzsMQrXuUVRZ')
    return api