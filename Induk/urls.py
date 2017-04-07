"""Induk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('tax.urls', namespace = "tax")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^learning/', include('learning.urls', namespace="learning")),
    url(r'^report/', include('report.urls', namespace="report")),
    url(r'', include('notice.urls', namespace="notice")),
    url(r'^questions/', include('questions.urls', namespace="questions")),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/register/$', UserCreateView.as_view(), name = 'register'),
    # url(r'^accounts/register/done/$', UserCreateDoneTV.as_view, name = 'register_done'),
]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)