#Vanilla ArmPrime 
###No Docker

*For raspberry pi running raspbian*


###### OS SETUP:
```bash
sudo apt-get install -y python3 python3-dev python3-setuptools nginx supervisor postgresql-client
sudo apt-get update
sudo apt-get install -y software-properties-common python3-software-properties
```

###### PYTHON3 SETUP:
```bash
sudo apt-get install python3-venv
pip3 install --upgrade pip
sudo pip3 install -r requirements.txt
```


[comment]: <> (###### POSTGRESQL SETUP:)

[comment]: <> (```bash)

[comment]: <> (ssh -L 3333:127.0.0.1:<remote mysql port> <username>@<remote host> -N)

[comment]: <> (```)

###### POST-INSTALLATION OF ARMPRIME
```bash
pip install django-redis    ///maybe useless
redis-cli config set notify-keyspace-events KEA
# sudo -u postgres psql -U postgres postgres -c 'create extension hstore;'
python3 manage.py makemigrations chat krogoth_3rdparty_api krogoth_examples krogoth_apps krogoth_social moho_extractor krogoth_gantry krogoth_core krogoth_admin
python3 manage.py makemigrations
python3 manage.py migrate
```


[comment]: <> (###### POSTGRESQL SETUP:)

[comment]: <> (```bash)

[comment]: <> (sudo apt-get update)

[comment]: <> (sudo apt-get install postgresql postgresql-contrib)

[comment]: <> (sudo -u postgres psql postgres)

[comment]: <> (\password postgres)

[comment]: <> (```)


###### RUN VENV: (optional)
```bash
python3 -m venv ARM_ENV
source ./ARM_ENV/bin/activate
```


###### POST-INSTALLATION OF ARMPRIME
```bash
python3 manage.py makemigrations krogoth_gantry
python3 manage.py migrate
python3 manage.py installdjangular
python3 manage.py collectdvc
python3 manage.py collectstatic
python3 manage.py createsuperuser
```


*Django-Krogoth/jawn/uwsgi.py* needs to have a block removed.
##BEFORE:
```python3
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


### UNCOMMENT THIS BLOCK TO USE MANAGE.PY RUNSERVER (python3 manage.py runserver 0.0.0.0:8000)
# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jawn.settings')
# application = get_wsgi_application()
```


##AFTER:
```python3
# import os
# import sys
# sys.path.insert(0, os.path.abspath('..'))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jawn.settings')
# from django.core.wsgi import get_wsgi_application
# from django.conf import settings
# from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
# _django_app = get_wsgi_application()
# _websocket_app = uWSGIWebsocketServer()
# def application(environ, start_response):
#     if environ.get('PATH_INFO').startswith(settings.WEBSOCKET_URL):
#         return _websocket_app(environ, start_response)
#     return _django_app(environ, start_response)



### UNCOMMENT THIS BLOCK TO USE MANAGE.PY RUNSERVER (python3 manage.py runserver 0.0.0.0:8000)
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jawn.settings')
application = get_wsgi_application()

```