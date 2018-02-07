from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.getAllPosts, name='home'),
    url(r'^posts/$', views.getAllPosts, name ='getAllPosts'),
    url(r'^categories/$', views.getAllCategories, name = 'getAllCategories'),
    url(r'^profile/$', views.getUserProfile, name='getUserProfile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^categories/(?P<slug>[\w\-]+)/$', views.getCategory, name='getCategory'),   
    url(r'^author/(?P<slug>[\w\-]+)/public/posts/$', views.getAuthorPosts, name='getAuthorPosts'),
    url(r'^posts/(?P<slug>[\w\-]+)/$', views.getPost, name='getPost'),
    url(r'^posts/(?P<slug>[\w\-]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
   
]