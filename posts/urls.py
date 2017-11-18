from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.getAllPosts, name ='getAllPosts'),
	url(r'^categories/$', views.getAllCategories, name = 'getAllCategories'),
	url(r'^home/$', views.home, name='home')
]