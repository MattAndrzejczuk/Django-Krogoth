"""

 * KROGOTH v0.6.98
 * Copyright (C) 2017 Matt Andrzejczuk < matt@jawn.it >

 * KROGOTH can not be copied and/or distributed without the express
 * permission of Matt Andrzejczuk.

 * December 14th, 2017

"""

import os
import socket
import subprocess

from django.core.mail import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ic*v=-p%!6#0ki%kj2l&@4e_a_j!7xm7g9wmxu%8f$9xj*2ht'

DEBUG = True
ALLOWED_HOSTS = ['*']



# App will serve frontend from '/static/compiled' rather than slowly generating
# frontend code dynamically. Use True for production.
STATIC_KROGOTH_MODE = False




# Application definition
REST_FRAMEWORK = {
    'PAGE_SIZE': 80,
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
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     'rest_framework.throttling.ScopedRateThrottle',
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ),
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '28100/day',
    #     'user': '20010/day'
    # }
}
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
INSTALLED_APPS = (
    'suit',
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
    'django.contrib.sites',
    'ws4redis',
    'rest_framework_docs',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_framework_swagger',
    'chat',
    'krogoth_core',
    'krogoth_apps',
    'moho_extractor',
    'krogoth_gantry',
    'krogoth_3rdparty_api',
    'krogoth_social',
    'krogoth_admin',
    'djangular_dashboard',
    'django_filters',
    'kbot_lab',
    'krogoth_examples',
    'django_extensions',
)

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




db_name = 'jawn'
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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# static files:
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = ('/usr/src/volatile/static/')

# user uploads root path:
MEDIA_ROOT = '/usr/src/persistent/media/'
MEDIA_URL = '/media/'

# other
SITE_ID = 2
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'chat.serializers.GetUserSerializer',
}
APPEND_SLASH = True







# <WebSocket Config>
#    - WebSocket messages are stored in a Redis DB, not in PostgreSQL DB.
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
# JavaScript mode will assume user access token is not in header of socket connection.
JAVASCRIPT_MODE = True
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
# </WebSocket Config>
















# Krogoth Initialization.
# don't touch this, it just prints version info for Python and Django.
DJANGULAR_STATIC = 'krogoth_gantryStaticFiles'
import django
import rest_framework
try:
    print('')
    print('\033[35mInitializing Django ' +
          str(django.VERSION[0]) + '.' + str(django.VERSION[1]) + '.' + str(django.VERSION[2]) + '\033[0m')
    print('\033[95mDjango REST Framework ' + str(rest_framework.VERSION) + '\033[0m')

    # GET LAZARUS BUILD VERSION:
    bash_cmd = ['git', 'rev-list', '--count', 'master']
    get_build_cmd = str(subprocess.check_output(bash_cmd))
    current_build_1 = ''
    current_build_2 = ''
    try:
        current_build_1 = ('0.' + str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", "")) + '.'
        current_build_2 = (str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", ""))[1:]
    except:
        print('failed to check version!!!')
    if current_build_2 == '00':
        current_build_2 = '0'
    else:
        rm_0s = current_build_2.replace('10', '1').replace('20', '2').replace('30', '3').replace('40', '4')
        current_build_2 = rm_0s.replace('50', '5').replace('60', '6').replace('70', '7').replace('80', '8').replace(
            '90', '9')

    APP_VERSION = current_build_1[:3] + "." + current_build_2
    print('\033[1m\033[32mKrogoth ' + APP_VERSION + ' \033[0m\033[0m')
    print()
except:
    print('Django initialized, but the version is unknown... wtf?')

print("RC Soon")


# print("POSTGRES: ")
# print(os.environ["POSTGRES_ENV_POSTGRES_USER"])
# print(os.environ["POSTGRES_ENV_POSTGRES_PASSWORD"])
# print(os.environ["POSTGRES_PORT_5432_TCP_ADDR"])
# print(os.environ["POSTGRES_PORT_5432_TCP_PORT"])