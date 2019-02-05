import os
import time
from subprocess import Popen, PIPE


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


class Installaton():

    def __init__(self):
        print("installation obj called...")

    @classmethod
    def execute(cls, cmd, installation_phase):
        """
        Run a command in the terminal.

        """

        time.sleep(1)
        args = cmd.split(" ")
        print(bc.purple + "RUNNING COMMAND: " + bc.ENDC + bc.green + str(args) + bc.ENDC)

        proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output = proc.communicate(timeout=15)

        user_input = input("continue? (y, n)       (yo - yes and print output)")
        if user_input.upper() != "Y":
            exit()
        elif user_input == "yo":
            print(bc.blue + str(output) + bc.ENDC)
            time.sleep(1)

    @classmethod
    def destroy_docker(cls):
        """
        Completely wipe out all docker containers running on this machine.

        """
        cmd = ('sh KILL_ALL_.sh')
        os.system(cmd)


WORK_DIR = os.getcwd()
PARENT_DIRPATH = os.path.abspath(os.path.join(WORK_DIR, os.pardir))
installer = Installaton()

print("WORKING IN " + bc.lightblue + WORK_DIR + bc.ENDC)

DOCKER_SQL_CONTAINERNAME = "postgres"
SQL_USER = "jawn"
SQL_PASS = "xzxzf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79xzxz"
SQL_PUBLIC_PORT = "8091"
SQL_PRIVATE_PORT = "5432"
SQL_ARGS = "-e POSTGRES_USER=" + \
           SQL_USER + " -d -p " + \
           SQL_PUBLIC_PORT + ":" + \
           SQL_PRIVATE_PORT + " " + \
           DOCKER_SQL_CONTAINERNAME



print(bc.BOLD + bc.blue + "DESTORYING PREVIOUS KROGOTH " + PARENT_DIRPATH + bc.ENDC + bc.ENDC)
time.sleep(1)
installer.destroy_docker()

cmd = ("docker build -t mattjawn/armprime ./app/")
installer.execute(cmd, bc.yellow + "DOCKER BUILD" + bc.ENDC)

db_args = "-e POSTGRES_USER=jawn -d -p 8091:5432 postgres"
db_pw = "58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9"

cmd = ("docker run --name armprime-postgres -e POSTGRES_PASSWORD=" + SQL_PASS + " " + SQL_ARGS)
Installaton.execute(cmd, cmd)

cmd = ("docker run -d -p 7070:6379 --name=armprime-redis redis")
Installaton.execute(cmd, cmd)

cmd = (
        'docker run -d -p 80:80 -v "' + PARENT_DIRPATH + '":/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime')
Installaton.execute(cmd, cmd)

cmd1 = ('docker exec armprime-redis redis-cli config set notify-keyspace-events KEA')
Installaton.execute(cmd1, "armprime-redis")

# CREATE USER 'jawn' with pass: '123123'
cmd = ('docker exec -it armprime-postgres useradd -p $(openssl passwd -1 123123) jawn')
Installaton.execute(cmd, cmd)

cmd = ("docker exec -it --user jawn armprime-postgres psql jawn -c 'create extension hstore;'")
Installaton.execute(cmd, cmd)




### ---====== remove previous migrations ======---
cmd = ('sleep 1')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../krogoth_chat/migrations')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../krogoth_3rdparty_api/migrations')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../krogoth_examples/migrations')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../krogoth_admin/migrations')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../krogoth_apps/migrations')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../krogoth_social/migrations')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../moho_extractor/migrations')
Installaton.execute(cmd, cmd)

cmd = ('rm -R ../kbot_lab/migrations')
Installaton.execute(cmd, cmd)

cmd = ('sleep 1')
Installaton.execute(cmd, cmd)



### ---====== make new migrations ======---
cmd = (
    'docker exec -it armprime ./manage.py makemigrations krogoth_core moho_extractor krogoth_3rdparty_api krogoth_admin krogoth_social kbot_lab krogoth_chat krogoth_examples kbot_lab krogoth_gantry')
Installaton.execute(cmd, cmd)

cmd = ('docker exec -it armprime ./manage.py migrate')
Installaton.execute(cmd, bc.lightgreen + cmd)

cmd = ('sleep 2')
Installaton.execute(cmd, cmd)




### ---====== install krogoth gantry units ======---
cmd = ('docker exec -it armprime ./manage.py installdjangular')
Installaton.execute(cmd, bc.lightgreen + cmd)

print(bc.lightgreen + "./manage.py collectdvc" + bc.ENDC)
ak_install = ['docker', 'exec', '-it', 'armprime', './manage.py', 'collectdvc']
with Popen(ak_install, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
    proc.communicate(b"")

print(bc.lightgreen + "./manage.py collectstatic" + bc.ENDC)
static_col = ['docker', 'exec', '-it', 'armprime', './manage.py', 'collectstatic']
with Popen(static_col, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
    proc.communicate(b"")


### ---====== install global fuse units ======---
Installaton.execute(cmd, "Installing Default Templates" + bc.ENDC)
cmd = ('sleep 2')
Installaton.execute(cmd, bc.lightgreen + "INSTALLATION COMPLETED" + bc.ENDC)
Installaton.execute(cmd, bc.lightgreen + "CREATING SUPER USER: " + bc.ENDC)


### ---====== fin ======---
os.system('docker exec -it armprime ./manage.py createsuperuser')