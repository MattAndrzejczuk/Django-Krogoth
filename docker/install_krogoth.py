import os
# from subprocess import DEVNULL, STDOUT, check_call
import time
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



cmd = ('sh KILL_ALL_.sh')

cwd = os.getcwd()
parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))



OUTPUT_ENABLED = False

def execute(cmd, always_display):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if OUTPUT_ENABLED == True or always_display == "NEEDED":
        print(out.decode("utf-8"))
    print(always_display)



print(bc.bold + bc.blue + "INSTALLING KROGOTH " + parent_dir + bc.ENDC + bc.ENDC)
time.sleep(1)
cmd = ("docker build -t mattjawn/armprime ./app/")
execute(cmd, bc.yellow+"DOCKER BUILD"+bc.ENDC)
db_args = "-e POSTGRES_USER=jawn -d -p 8091:5432 postgres"
db_pw = "58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9"
cmd = ("docker run --name armprime-postgres -e POSTGRES_PASSWORD="+db_pw+" "+ db_args)

execute(cmd, bc.yellow + "DOCKER RUNNING Postgres" + bc.ENDC)
cmd = ("docker run -d -p 7070:6379 --name=armprime-redis redis")
execute(cmd, bc.yellow + "DOCKER RUNNING Redis" + bc.ENDC)
cmd = ('docker run -d -p 80:80 -v "'+parent_dir+'":/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime')
execute(cmd, bc.yellow + "DOCKER RUNNING Django" + bc.ENDC)
cmd = ('clear')
execute(cmd, bc.yellow + "DOCKER RUNs finished " + bc.ENDC)


# print(bc.pink + "INSTALLING KROGOTH: " + parent_dir + bc.ENDC)
# os.system('sh run-docker-installed.sh')

cmd = ('docker exec -it armprime pip3 install django-redis==4.8.0')
execute(cmd, bc.purple+"install django-redis"+bc.ENDC)
cmd = ('docker exec -it armprime apt-get install -y -qq nodejs')
execute(cmd, bc.purple+"nodejs"+bc.ENDC)
cmd = ('docker exec -it armprime apt-get install -qq npm')
execute(cmd, bc.purple+"npm"+bc.ENDC)
cmd = ('sleep 1')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('docker exec armprime-redis redis-cli config set notify-keyspace-events KEA')
execute(cmd, bc.lightblue+"armprime-redis"+bc.ENDC)
cmd = ("echo 'creating psql extension hstore...'")
execute(cmd, bc.lightblue+"creating psql extension hstore..."+bc.ENDC)
cmd = ('sleep 1')
execute(cmd, bc.lightblue+""+bc.ENDC)
# CREATE USER 'jawn' with pass: '123123'
cmd = ('docker exec -it armprime-postgres useradd -p $(openssl passwd -1 123123) jawn')
execute(cmd, bc.lightblue+""+bc.ENDC)
# cmd = ("docker exec -it --user postgres armprime-postgres psql jawn -c 'create extension hstore;'")
cmd = ("docker exec -it armprime-postgres psql -U jawn postgres -c 'create extension hstore;'")
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('sleep 1')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../chat/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../krogoth_3rdparty_api/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../krogoth_examples/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../krogoth_admin/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../krogoth_apps/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../krogoth_social/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../moho_extractor/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../kbot_lab/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../LazarusIII/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../LazarusIV/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('rm -R ../LazarusV/migrations')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py makemigrations chat krogoth_3rdparty_api krogoth_examples krogoth_apps krogoth_social moho_extractor krogoth_gantry krogoth_core krogoth_admin')
execute(cmd, bc.lightblue+""+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py migrate')
execute(cmd, bc.lightgreen+""+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py installdjangular')
execute(cmd, bc.lightgreen+""+bc.ENDC)
cmd = ('sleep 1')
execute(cmd, bc.lightgreen+"CREATING SUPER USER: "+bc.ENDC)
os.system('docker exec -it armprime ./manage.py createsuperuser')
#execute(cmd, bc.lightgreen+""+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py collectstatic')
execute(cmd, bc.lightgreen+"Collecting Static"+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py collectdvc')
execute(cmd, bc.lightblue+"Installing Default Templates"+bc.ENDC)
cmd = ('sleep 2')
execute(cmd, bc.lightgreen + "INSTALLATION COMPLETED" + bc.ENDC)
os.system('docker exec -it armprime uwsgi ../runserver_uwsgi.ini')
