from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.report_index, name = 'report_index'),

	url(r'^(?P<company>\w+)/$', views.report_list, name="report_list"),
	url(r'^(?P<company>\w+)/new/$', views.report_new, name="report_new"),
	url(r'^(?P<company>\w+)/(?P<pk>\d+)/$', views.report_detail, name="report_detail"),
	url(r'^(?P<company>\w+)/(?P<pk>\d+)/edit/$', views.report_edit, name="report_edit"),
	url(r'^(?P<company>\w+)/(?P<pk>\d+)/del/$', views.report_del, name="report_del"),
	url(r'^(?P<company>\w+)/(?P<pk>\d+)/comment/$', views.report_comment, name="report_comment"),
]
