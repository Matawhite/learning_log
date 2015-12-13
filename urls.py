"""Defines URL patterns for learning_logs"""

from django.conf.urls import urls
from . import views

urlpatters = [
#home page
url(r'^$', views.index, name='index'),
]