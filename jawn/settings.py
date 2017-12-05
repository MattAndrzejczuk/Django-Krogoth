"""
Django settings for jawn project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import subprocess
from django.core.mail import *
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGULAR_STATIC = 'DjangularStaticFiles'



FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ic*v=-p%!6#0ki%kj2l&@4e_a_j!7xm7g9wmxu%8f$9xj*2ht'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

REST_FRAMEWORK = {
    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',),
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


INSTALLED_APPS = (
    'suit',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.twitter',
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'ws4redis',
    'rest_framework_docs',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'fcm_django',
    'chat',
    'lazarus',
    'LazarusII',
    'LazarusIV',
    'LazarusV',
    'dynamic_lazarus_page',
    'DatabaseSandbox',
    'PhotoGalleryManager',
    'GeneralWebsiteInfo',
    'LazarusDatabase',
    'Djangular',
    'CommunityForum',
    'ModBuilder',
    'djangular_dashboard',
    'django_filters',
    'LazarusPublicAssets',
    'LazarusPublisherTest',
    'filebrowser',
    'grappelli',
)
#   'dbbackup',


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'jawn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ws4redis.context_processors.default',
            ],
        },
    },
]

WSGI_APPLICATION = 'jawn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

db_name = 'jawn6'
if os.path.exists('/usr/src/app/LazarusIII/GAFDump_EXE_Cavedog_Assets'):
    db_name = 'jawn5'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': os.environ["POSTGRES_ENV_POSTGRES_USER"],
        'PASSWORD': os.environ["POSTGRES_ENV_POSTGRES_PASSWORD"],
        'HOST': os.environ["POSTGRES_PORT_5432_TCP_ADDR"],
        'PORT': os.environ["POSTGRES_PORT_5432_TCP_PORT"],
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'jawn',
#         'USER': 'ubuntu',
#         'PASSWORD': 'sau4tgiudnf',
#         'HOST': '12.226.201.62',
#         'PORT': '32769',
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'),
    #'/Users/Dominooch/Dropbox/Dev/theEmpire/static/',
)



STATIC_ROOT = ('/usr/src/volatile/static/')
#STATIC_ROOT = ('/usr/arm-prime/static/')

MEDIA_ROOT = '/usr/src/persistent/media/'
MEDIA_URL = '/media/'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://" + os.environ["REDIS_PORT_6379_TCP_ADDR"] + ":" + os.environ["REDIS_PORT_6379_TCP_PORT"] + "/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
        }
    }
}

WEBSOCKET_URL = '/ws/'

# Set to true if you want to use WebSockets for JavaScript
# If false, you will not be able to connect to WebSocket with Auth Token in the headers
JAVASCRIPT_MODE = True

# Set the number of seconds each message shall persited
WS4REDIS_EXPIRE = 2
WS4REDIS_HEARTBEAT = '--heartbeat--'
WS4REDIS_PREFIX = 'demo'
WS4REDIS_CONNECTION = {
    'host': os.environ["REDIS_PORT_6379_TCP_ADDR"],
    'port': os.environ["REDIS_PORT_6379_TCP_PORT"],
    'db': 0,
    'password': None,
}

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_PREFIX = 'session'
SESSION_REDIS_HOST = os.environ["REDIS_PORT_6379_TCP_ADDR"]
SESSION_REDIS_PORT = os.environ["REDIS_PORT_6379_TCP_PORT"]

SITE_ID = 2

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'chat.serializers.GetUserSerializer',
}

###
# SQL BACKUP
#
#  TODO: figure out how to get this thing working.
#
# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {'location': '/usr/src/app/backupSQL'}
# pip3 install django-dbbackup
###

APPEND_SLASH = True


if JAVASCRIPT_MODE == True:
    print('\n\033[34mWebSockets are in JavaScript Mode.\033[0m')
else:
    print('\n\033[35mWebSockets are in native mode, Auth headers required for a connection.\033[0m')

import django
import rest_framework
try:
    print('')
    print('\033[90mInitializing Django ' +
          str(django.VERSION[0]) + '.' + str(django.VERSION[1]) + '.' + str(django.VERSION[2]) + '\033[0m')
    print('\033[96mDjango REST Framework ' + str(rest_framework.VERSION) + '\033[0m')
    print('')
except:
    print('Django initialized, but the version is unknown... wtf?')

print("POSTGRES: ")
print(os.environ["POSTGRES_ENV_POSTGRES_USER"])
print(os.environ["POSTGRES_ENV_POSTGRES_PASSWORD"])
print(os.environ["POSTGRES_PORT_5432_TCP_ADDR"])
print(os.environ["POSTGRES_PORT_5432_TCP_PORT"])


# PUSH NOTIFICATIONS:
FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AAAAcXA4kTc:APA91bGhguFF3Q28Mm8mJWB-iiXWaMQRxUWsLT8b0ZFspZ66MPOXnrWqzwqx2ek3MCG0WoPxWtgXJvc_qwtIz2glpCRN_rRSMr-AHRfty0f1sppcp1ehRgkEfel6uoqo-28JzKJ_Q-lG"
}



PUBLIC_EXTRACTED_HPIs = '/usr/src/persistent/media/Processed_HPI_Archives/'
if not os.path.exists(PUBLIC_EXTRACTED_HPIs):
    os.makedirs(PUBLIC_EXTRACTED_HPIs)