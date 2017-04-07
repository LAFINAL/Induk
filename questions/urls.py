from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.questions_list, name="questions_list"),
    url(r'^(?P<pk>\d+)/$', views.questions_detail, name="questions_detail"),
    url(r'^new/$', views.questions_new, name="questions_new"),
    url(r'^(?P<pk>\d+)/edit/$', views.questions_edit, name="questions_edit"),
    url(r'^(?P<pk>\d+)/del/$', views.questions_del, name="questions_del"),
    url(r'^(?P<pk>\d+)/comment/$', views.questions_comment, name="questions_comment"),
]
	
