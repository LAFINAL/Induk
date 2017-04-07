"""
Django settings for Induk project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
# 휴이스의 BASE_DIR os.path가 빠진 이유는 from os.path import abspath, dirname을 import 함

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a#oy4p0#1giv0h^kv6wtlbixgqu$2cx7h^&s58-2n7#e2&jtw%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


AUTH_USER_MODEL = 'accounts.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    # python manage.py startapp...
    # local Apps

    'accounts',
    'learning',
    'report',
    'notice',
    'questions',
    'lib',
    # 'staff',

    'bootstrap3',
    # 'disqus',
]

DISQUS_WEBSITE_SHORTNAME = 'indukcomments'
SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Induk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(BASE_DIR, "Induk", "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Induk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로. 이 최상위 경로 자체는 실제 파일이나
# 디렉토리가 아니며, URL로만 존재하는 단위. findstatic 명령어로 탐색되는
# 정적 파일 경로에 STATIC_URL 경로를 합치면 실제 웹에서 접근 가능한 URL이 된다.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 개발단계에서는 필요없는 코드. 실제 collectstatic 명령어를 수행하여
# STATICFILES_DIRS 나 앱 디렉터리에 있는 static 디렉터리 안에 있는
# 파일을 STATIC_ROOT에 모으는데, STATICFILES_DIRS 에 지정된 경로인 경우
# 따로 명시한 접두사
# STATIC_ROOT 경로는 STATICFILES_DIRS 등록된 경로와 같은 경로가 있어서는 안된다.
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
MEDIA_URL = '/uploaded_files/'
#LOGIN_URL = 'accounts/login/'
#LOGOUT_URL = 'accounts/logout/'
#어차피 내가 설정해준 거랑 같아서 다 주석처리해도 되는 것임.
LOGIN_REDIRECT_URL='/main'
# LOGIN_URL =
# 로그인이 필요해서 로그인 페이지로 리다이렉트시키고자 할 때 사용하는 URL. 특히 login_required() 데코레이터에서
# 사용한다. 만일 이 항목을 지저하지 않으면 디폴트로 /accounts/login/  URL 을 사용한다.
# LOGOUT_URL =
# 로그아웃시키고자 할 때 사용하는 URL. 만일 이 항목을 지정하지 않으면 디폴트로
# /accounts/logout/  URL을 사용한다.
# LOGIN_REDIRECT_URL =
# contrib.auth.login() 뷰는 로그인 처리가 성공한 후에 next 파라미터로 지정한 URL로 리다이렉트 시킨다. 만일
# settings.py 파일에 이 항목을 지정하지 않으면 디폴트로 /accounts/profile/   URL을 사용한다.



##message
from django.contrib.messages import constants as messages_constants
MESSAGE_TAGS = {messages_constants.ERROR: 'danger'}
