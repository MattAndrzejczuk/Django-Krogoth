"""
WSGI config for jawn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jawn.settings')

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

_django_app = get_wsgi_application()
_websocket_app = uWSGIWebsocketServer()


def application(environ, start_response):
    if environ.get('PATH_INFO').startswith(settings.WEBSOCKET_URL):
        return _websocket_app(environ, start_response)
    return _django_app(environ, start_response)


# docker run -d -P --name=jawn-redis redis
# docker run -d -P -e POSTGRES_USER=ubuntu -e POSTGRES_PASSWORD=sau4tgiudnf --name=jawn-postgres postgres
# docker run -d -p 80:80 -v ~/jawn-backend/:/opt/django/app/ --link jawn-postgres:postgres --link jawn-redis:redis --name=jawn-backend domface/jawn:1.2

# docker run -d -p 80:80 -v ~/portfolio-app/:/opt/django/app/ --link jawn-postgres:postgres --link jawn-redis:redis --name=morado-backend domface/jawn:1.2

# docker run -d -P --name=morado-redis redis && docker run -d -P -e POSTGRES_USER=ubuntu -e POSTGRES_PASSWORD=sau4tgiudnf --name=morado-postgres postgres && ./ma