from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
	url(r'^login/$', views.login, kwargs={'template_name': 'accounts/login.html'} ,name = 'login'),
	url(r'^signup/$', views.signup, name = 'signup'),
	url(r'^pw_reset/$', views.password_reset, name='password_reset'), # 직접 비밀번호 바꾸는 경우
	url(r'^pw_admin/$', views.password_reset_admin, name='password_reset_admin'), # 관리자가 비밀번호 리셋 시키는 경우
	# url(r'^register/$', UserCreateView.as_view(), name = 'register'),
    #url(r'^register/done/$', UserCreateDoneTV.as_view(), name = 'register_done'),
	#url(r'^logout/$', logout_page),
	url(r'^logout/$', logout, kwargs={'next_page': '/'}, name='logout'),
	url(r'^mypage/$', views.mypage, name='mypage'),
]
