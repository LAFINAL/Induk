from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, "..", "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'induk'),
        'USER': os.environ.get('DJANGO_DATABASE_USER', 'ubuntu'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', 'bhunjimko123'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', '127.0.0.1'),
    }
}


# AWS S3
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_SECURE_URLS = False													# https
#
# AWS_STORAGE_BUCKET_NAME = 'bucket_name'										# AWS S3 버켓 이름
# AWS_ACCESS_KEY_ID = 'xxxxxxxxx'												# access key
# AWS_SECRET_ACCESS_KEY = 'yyyyyyyyy'											# secret access key
#
# AWS_REGION = 'ap-northeast-2'												# Seoul Region
# AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
#
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = "http://%s/" % AWS_S3_CUSTOM_DOMAIN
# MEDIA_URL = 'http://%s/' % AWS_S3_CUSTOM_DOMAIN
