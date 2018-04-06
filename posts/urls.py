from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.getPosts, name='getPosts'),
    url(r'^(?P<parentCatSlug>[\w\-]+)/(?P<categorySlug>[\w\-]+)/posts/$', views.getCategories, name = 'getCategories'),
    url(r'^profile/$', views.getUserProfile, name='getUserProfile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^categories/(?P<categorySlug>[\w\-]+)/$', views.getCategory, name='getCategory'),   
    url(r'^author/(?P<slug>[\w\-]+)/public/posts/$', views.getAuthorPosts, name='getAuthorPosts'),
    url(r'^posts/(?P<slug>[\w\-]+)/$', views.getPost, name='getPost'),
    url(r'^posts/(?P<slug>[\w\-]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'privacypolicy$', views.privacypolicy, name='privacypolicy'),
]