from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.learning_list, name = "learning_list"),
    url(r'^(?P<pk>\d+)/$', views.learning_detail, name="learning_detail"),
    url(r'^new/$', views.learning_new, name="learning_new"),
    url(r'^(?P<pk>\d+)/edit/$', views.learning_edit, name="learning_edit"),
    url(r'^(?P<pk>\d+)/del/$', views.learning_del, name="learning_del"),
    url(r'^(?P<pk>\d+)/comment/$', views.learning_comment, name="learning_comment"),
]
