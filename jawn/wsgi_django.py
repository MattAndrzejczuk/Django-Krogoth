# entry point for the Django loop
from django.core.wsgi import get_wsgi_application
import uwsgi
from uwsgidecorators import timer
from django.utils import autoreload


# @timer(1)
# def change_code_gracefull_reload(sig):
    # if autoreload.file_changed():
    # if autoreload.code_changed():
    #     uwsgi.reload()


application = get_wsgi_application()