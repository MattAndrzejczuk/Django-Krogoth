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

def cstr(i) -> str:
    return '\033['+str(i)+'m'


class AKInstallation():

    def __init__(self):
        print("installation obj called...")

    @classmethod
    def print_terminal_input(cls, args):
        loop = 0
        for cmd in args:
            if loop == 0:
                print(bc.green + cmd + bc.ENDC, end='')
            else:
                print(bc.purple + cmd + bc.ENDC, end='')
            if len(args) == loop + 1:
                print(";")
            loop += 1


    @classmethod
    def execute(cls, cmd, installation_phase):
        """
        runs a terminal command and waits for completion to then print all output at once.

        :param cmd: the full terminal command
        :param installation_phase: the current command number (1,2,3,4,...x)
        :return: void
        """


        args = cmd.split(" ")
        cls.print_terminal_input(args)

        proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = proc.communicate("")

        term_reply = output.decode('utf-8')
        term_errors = err.decode('utf-8')


        print(cstr(104) + cstr(37) + term_reply + cstr(0) + cstr(0))


        if len(term_errors) > 1 and args[0] != 'rm':
            print(cstr(107) + cstr(91) + term_errors + cstr(0) + cstr(0))
            os.system("say 'Warning, " + args[0] + " error.'")
            # user_input = input("continue installation anyway? (y, n)")
            # if user_input.upper() == "N":

        # for line in term_reply:
        #     try:
        #         print(bc.lightblue + line + bc.ENDC, end='')
        #     except:
        #         pass
        # for line in term_errors:
        #     try:
        #         print(bc.red + line.decode('UTF-8') + bc.ENDC, end='')
        #     except:
        #         pass





    @classmethod
    def show_realtime_out(cls, proc: Popen):
        """
        prints output in realtime

        :param proc: Popen with stdout
        :return: void
        """
        for line in proc.stdout:
            print(bc.cyan + line.decode('UTF-8') + bc.ENDC, end='')

    @classmethod
    def execute_realtime_out(cls, cmd: str, installation_phase):
        """
        runs a terminal command and gets all output in realtime.

        :param cmd: the full terminal command
        :param installation_phase: the current command number (1,2,3,4,...x)
        :return: void
        """

        args = cmd.split(" ")
        cls.print_terminal_input(cmd)
        proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        cls.show_realtime_out(proc)
        proc.wait(999)


    @classmethod
    def destroy_docker(cls):
        """
        Completely wipe out all docker containers running on this machine.

        """
        cmd = ('sh KILL_ALL_.sh')
        os.system(cmd)


WORK_DIR = os.getcwd()
PARENT_DIRPATH = os.path.abspath(os.path.join(WORK_DIR, os.pardir))
installer = AKInstallation()

print(bc.lightblue + "WORKING IN " + bc.ENDC + bc.pink + WORK_DIR + bc.ENDC)

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


os.system('say -v Karen "welcome."')


print(bc.BOLD + bc.blue + "DESTORYING PREVIOUS KROGOTH " + PARENT_DIRPATH + bc.ENDC + bc.ENDC)
installer.destroy_docker()
o = input("...")
cmd_n01 = ("docker build -t mattjawn/armprime ./app/")
installer.execute_realtime_out(cmd_n01, "")

db_args = "-e POSTGRES_USER=jawn -d -p 8091:5432 postgres"
db_pw = "58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9"

cmd_n02 = ("docker run --name armprime-postgres -e POSTGRES_PASSWORD=" + SQL_PASS + " " + SQL_ARGS)
AKInstallation.execute_realtime_out(cmd_n02, cmd_n02)

cmd_n03 = ("docker run -d -p 7070:6379 --name=armprime-redis redis")
AKInstallation.execute_realtime_out(cmd_n03, cmd_n03)

cmd_n04 = (
        'docker run -d -p 80:80 -v "' + PARENT_DIRPATH + '":/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime')
AKInstallation.execute_realtime_out(cmd_n04, cmd_n04)

cmd_n05 = ('docker exec armprime-redis redis-cli config set notify-keyspace-events KEA')
AKInstallation.execute_realtime_out(cmd_n05, "armprime-redis")

# CREATE USER 'jawn' with pass: '123123'
cmd_n06 = ('docker exec -it armprime-postgres useradd -p $(openssl passwd -1 123123) jawn')
AKInstallation.execute_realtime_out(cmd_n06, cmd_n06)

cmd_n07 = ("docker exec -it --user jawn armprime-postgres psql jawn -c 'create extension hstore;'")
AKInstallation.execute_realtime_out(cmd_n07, cmd_n07)




### ---====== remove previous migrations ======---
cmd_n09 = ('rm -R ../krogoth_chat/migrations')
AKInstallation.execute_realtime_out(cmd_n09, cmd_n09)

cmd_n10 = ('rm -R ../krogoth_3rdparty_api/migrations')
AKInstallation.execute_realtime_out(cmd_n10, cmd_n10)

cmd_n11 = ('rm -R ../krogoth_examples/migrations')
AKInstallation.execute_realtime_out(cmd_n11, cmd_n11)

cmd_n12 = ('rm -R ../krogoth_admin/migrations')
AKInstallation.execute_realtime_out(cmd_n12, cmd_n12)

cmd_n13 = ('rm -R ../krogoth_apps/migrations')
AKInstallation.execute_realtime_out(cmd_n13, cmd_n13)

cmd_n14 = ('rm -R ../krogoth_social/migrations')
AKInstallation.execute_realtime_out(cmd_n14, cmd_n14)

cmd_n15 = ('rm -R ../moho_extractor/migrations')
AKInstallation.execute_realtime_out(cmd_n15, cmd_n15)

cmd_n16 = ('rm -R ../kbot_lab/migrations')
AKInstallation.execute_realtime_out(cmd_n16, cmd_n16)




### ---====== make new migrations ======---
cmd_n18 = (
    'docker exec -it armprime ./manage.py makemigrations krogoth_core moho_extractor krogoth_3rdparty_api krogoth_admin krogoth_social kbot_lab krogoth_chat krogoth_examples kbot_lab krogoth_gantry')
AKInstallation.execute_realtime_out(cmd_n18, cmd_n18)

cmd_n19 = ('docker exec -it armprime ./manage.py migrate')
AKInstallation.execute_realtime_out(cmd_n19, bc.lightgreen + cmd_n19)




### ---====== install krogoth gantry units ======---
cmd_n21 = ('docker exec -it armprime ./manage.py installdjangular')
AKInstallation.execute_realtime_out(cmd_n21, bc.lightgreen + cmd_n21)

print(bc.lightgreen + "./manage.py collectdvc" + bc.ENDC)
ak_install = ['docker', 'exec', '-it', 'armprime', './manage.py', 'collectdvc']
with Popen(ak_install, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
    proc.communicate(b"")

print(bc.lightgreen + "./manage.py collectstatic" + bc.ENDC)
static_col = ['docker', 'exec', '-it', 'armprime', './manage.py', 'collectstatic']
with Popen(static_col, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
    proc.communicate(b"")


### ---====== install global fuse units ======---


### ---====== fin ======---
os.system('docker exec -it armprime ./manage.py createsuperuser')