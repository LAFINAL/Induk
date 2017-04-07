from django.conf.urls import url
from . import views

urlpatterns = [
#	url(r'^$', views.index, name = 'notice.index'),
	url(r'^$', views.index, name = "index"),
	url(r'^main$', views.main, name = "main"),
    url(r'^notice/$', views.notice_list, name="notice_list"),
    url(r'^notice/(?P<pk>\d+)/$', views.notice_detail, name="notice_detail"),
    url(r'^notice/new/$', views.notice_new, name="notice_new"),
    url(r'^notice/(?P<pk>\d+)/edit/$', views.notice_edit, name="notice_edit"),
    url(r'^notice/(?P<pk>\d+)/del/$', views.notice_del, name="notice_del"),
    url(r'^notice/(?P<pk>\d+)/comment/$', views.notice_comment, name="notice_comment"),
]
