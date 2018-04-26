# contactme/urls.py
from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^email$', views.emailView, name='email'),
    url(r'^success$', views.successView, name='success'),
]