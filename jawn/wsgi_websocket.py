import gevent.monkey
gevent.monkey.patch_thread()
from uwsgidecorators import timer
from django.utils import autoreload
import uwsgi


from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()

@timer(1)
def change_code_gracefull_reload(sig):
    if autoreload.code_changed():
        uwsgi.reload()