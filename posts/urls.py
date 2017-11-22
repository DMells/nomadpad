from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/$', views.getAllPosts, name ='getAllPosts'),
    url(r'^categories/$', views.getAllCategories, name = 'getAllCategories'),
    url(r'^profile/$', views.getUserProfile, name='getUserProfile'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^categories/(?P<postSlug>[-a-zA-Z0-9]+)/?$', views.getPost, name='getPost')
    url(r'^categories/(?P<pk>\d+)/$', views.getCategory, name='getCategory'),
    url(r'^posts/(?P<pk>\d+)/$', views.getPost, name='getPost'),
    #\d+ will match an integer of arbitrary size, and is used to retrieve
    # the category from the database. The pk bit is telling django to 
    # capture the value into a keyword argument named pk (via the view function).
    #Clicking on a link to a post will pass the post pk number to the url, which 
    # will be retrieved by the view and returned to the template.
    # url(r'^(?P<pk>\d+)/$', views.getCategory, name='getCategory')
]