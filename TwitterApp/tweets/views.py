from __future__ import unicode_literals
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
        fields = ['id', 'tag', 'author', 'message']


def post_list(request, template_name='tweets/post_list.html'):
    posts = tweets.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name='tweets/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tweets:post_list')
    return render(request, template_name, {'form': form})

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