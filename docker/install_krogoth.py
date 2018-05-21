import os
# from subprocess import DEVNULL, STDOUT, check_call

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEAL = '\033[96m'
    BLACK = '\033[97m'
    GRAY = '\033[90m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'



os.system('sh KILL_ALL_.sh')

cwd = os.getcwd()
parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))


print(bc.pink + "INSTALLING KROGOTH: " + parent_dir + bc.ENDC)
os.system("docker build -t mattjawn/armprime ./app/")
db_args = "-e POSTGRES_USER=jawn -d -p 8091:5432 postgres"
db_pw = "58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9"
os.system("docker run --name armprime-postgres -e POSTGRES_PASSWORD="+db_pw+" "+ db_args)
os.system("docker run -d -p 7070:6379 --name=armprime-redis redis")
os.system('docker run -d -p 80:80 -v "'+parent_dir+'":/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime')
os.system('clear')



# print(bc.pink + "INSTALLING KROGOTH: " + parent_dir + bc.ENDC)
# os.system('sh run-docker-installed.sh')

os.system('docker exec -it armprime pip3 install django-redis==4.8.0')
os.system('docker exec -it armprime apt-get install -y -qq nodejs')
os.system('docker exec -it armprime apt-get install -qq npm')
os.system('sleep 1')
os.system('docker exec armprime-redis redis-cli config set notify-keyspace-events KEA')
os.system("echo '\033[33m'")
os.system("echo 'creating psql extension hstore...'")
os.system('echo "\033[0m"')
os.system('sleep 1')
os.system("docker exec -it --user postgres armprime-postgres psql jawn -c 'create extension hstore;'")
os.system('sleep 1')
os.system('rm -R ../chat/migrations')
os.system('rm -R ../krogoth_3rdparty_api/migrations')
os.system('rm -R ../krogoth_examples/migrations')
os.system('rm -R ../krogoth_admin/migrations')
os.system('rm -R ../krogoth_apps/migrations')
os.system('rm -R ../krogoth_social/migrations')
os.system('rm -R ../moho_extractor/migrations')
os.system('rm -R ../kbot_lab/migrations')
os.system('rm -R ../LazarusIII/migrations')
os.system('rm -R ../LazarusIV/migrations')
os.system('rm -R ../LazarusV/migrations')
os.system('docker exec -it armprime ./manage.py makemigrations chat krogoth_3rdparty_api krogoth_examples krogoth_apps krogoth_social moho_extractor krogoth_gantry krogoth_core krogoth_admin')
os.system('docker exec -it armprime ./manage.py migrate')
os.system('docker exec -it armprime ./manage.py installdjangular')
os.system('sleep 1')
os.system("echo '\033[33m'")
os.system('docker exec -it armprime ./manage.py createsuperuser')
os.system('echo "\033[0m"')
os.system('echo "\033[35m"')
os.system('docker exec -it armprime ./manage.py collectstatic')
os.system('echo "\033[0m"')
os.system("echo '\033[34m'")
os.system('docker exec -it armprime ./manage.py collectdvc')
os.system('echo "\033[0m"')
os.system("echo '\033[32m'")
os.system('docker exec -it armprime uwsgi ../runserver_uwsgi.ini')
os.system('echo "\033[0m"')
