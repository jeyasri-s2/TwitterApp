"""TwitterApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path

# from tweets import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.post_list, name='post_list'),
#     url(r'^new$', views.post_create, name='post_new'),
#     url(r'^edit/(?P<pk>\d+)$', views.post_update, name='post_edit'),
#     url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
# ]
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tweets/', include('tweets.urls', namespace='tweets')),

]