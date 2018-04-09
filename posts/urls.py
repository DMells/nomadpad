from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.getPosts, name='getPosts'),
    url(r'^(?P<parentSlug>[\w\-]+)/(?P<catSlug>[\w\-]+)/$', views.getCategory, name='getCategory'),   
    url(r'^(?P<parentSlug>[\w\-]+)/(?P<catSlug>[\w\-]+)/(?P<postSlug>[\w\-]+)/$', views.getPost, name='getPost'),
    url(r'privacypolicy$', views.privacypolicy, name='privacypolicy'),
]
