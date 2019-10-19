"""
crudapp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin
from tweets import views

app_name = 'tweets'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create$', views.post_create, name='post_new'),
    url(r'^edit/(?P<pk>\d+)$', views.post_update, name='post_edit'),
    url(r'^delete/(?P<id>\d+)$', views.post_delete, name='post_delete'),
]
