import os
import time
from subprocess import Popen, PIPE
import subprocess


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
    return '\033[' + str(i) + 'm'


class AKInstallation():

    def __init__(self):
        print("installation obj called...")

    @classmethod
    def print_array_line(cls, args):
        try:
            loop = 0
            color1 = bc.green
            end1 = bc.ENDC
            color2 = bc.blue
            if type(args) == str:
                color1 = bc.lightgreen + bc.BOLD
                end1 = bc.ENDC + bc.ENDC
                args = args.split(" ")
            odd = True
            for cmd in args:
                if loop == 0:
                    print(color1 + cmd + end1, end=' ')
                else:
                    if odd == True:
                        odd = not odd
                        color2 = bc.pink
                    else:
                        color2 = bc.lightblue
                    print(color2 + cmd + end1, end=' ')
                if len(args) == loop + 1:
                    print("")
                loop += 1
        except:
            print(cstr(31) + "PRINT ARRAYLINE FAILURE: " + cstr(0) + cstr(95))
            print(args)
            print(cstr(0))

    @classmethod
    def execute(cls, cmd, installation_phase):
        """
        runs a terminal command and waits for completion to then print all output at once.

        :param cmd: the full terminal command
        :param installation_phase: the current command number (1,2,3,4,...x)
        :return: void
        """
        args = cmd.split(" ")
        cls.print_array_line(args)
        print(args)
        proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = proc.communicate("")
        term_reply = output.decode('utf-8')
        term_errors = err.decode('utf-8')
        print(cstr(104) + cstr(37) + term_reply + cstr(0) + cstr(0))
        try:
            if len(term_errors) > 1 and args[0] != 'rm':
                print(cstr(107) + cstr(91) + term_errors + cstr(0) + cstr(0))
                os.system("say 'Warning, " + args[0] + " error.'")
        except:
            print(cstr(31) + "CAUSE OF EXEC FAILURE: " + cstr(0) + cstr(35))
            print(cmd)
            print(cstr(0))

    @classmethod
    def execute_realtime_out(cls, cmd: str, installation_phase):
        """
        runs a terminal command and gets all output in realtime.

        :param cmd: the full terminal command
        :param installation_phase: the current command number (1,2,3,4,...x)
        :return: void
        """
        try:
            args = cmd.split(" ")
            with Popen(args, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
                for line in p.stdout:
                    print(line, end='')
            inp = input("press [ENTER] to skip.")
        except:
            print(cstr(31) + "CAUSE OF THE TERMINAL CMD FAILURE: " + cstr(0))
            print(cmd)

    @classmethod
    def destroy_docker(cls):
        """
        Completely wipe out all docker containers running on this machine.
        """
        cmd = ('sh KILL_ALL_.sh')
        os.system(cmd)


class InstallationRuntime():

    def __init__(self):
        WORK_DIR = os.getcwd()
        PARENT_DIRPATH = os.path.abspath(os.path.join(WORK_DIR, os.pardir))
        installer = AKInstallation()

        print(bc.lightblue + "WORKING IN " + bc.ENDC + bc.pink + WORK_DIR + bc.ENDC)

        DOCKER_SQL_NAME = "armprime-postgres"
        SQL_USER = "jawn"
        SQL_PASS = "xzxzf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79xzxz"
        SQL_PUBLIC_PORT = "8091"
        SQL_PRIVATE_PORT = "5432"
        SQL_ARGS = "-e POSTGRES_USER=" + \
                   SQL_USER + " -d -p " + \
                   SQL_PUBLIC_PORT + ":" + \
                   SQL_PRIVATE_PORT + " " + \
                   DOCKER_SQL_NAME

        MIGRATIONS_PT_1 = " krogoth_core moho_extractor krogoth_3rdparty_api krogoth_admin"
        MIGRATIONS_PT_2 = " krogoth_social kbot_lab krogoth_chat krogoth_examples kbot_lab krogoth_gantry"
        MAKE_MIGRATIONS = MIGRATIONS_PT_1 + MIGRATIONS_PT_2

        ORDERED_COMMANDS = []

        cmd_n01: str = "docker build -t mattjawn/armprime ./app/"
        cmd_n02: str = "docker run --name " + DOCKER_SQL_NAME + " " + SQL_ARGS
        cmd_n03: str = "docker run -d -p 7070:6379 --name=armprime-redis redis"
        cmd_n04: str = 'docker run -d -p 80:80 -v "' + PARENT_DIRPATH + \
                  '":/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime'
        cmd_n05: str = 'docker exec armprime-redis redis-cli config set notify-keyspace-events KEA'
        cmd_n06: str = 'docker exec -it armprime-postgres useradd -p $(openssl passwd -1 123123) jawn'
        cmd_n07: str = "docker exec -it --user jawn armprime-postgres psql jawn -c 'create extension hstore;'"
        cmd_n09: str = 'rm -R "../krogoth_chat/migrations"'
        cmd_n10: str = 'rm -R "../krogoth_3rdparty_api/migrations"'
        cmd_n11: str = 'rm -R "../krogoth_examples/migrations"'
        cmd_n12: str = 'rm -R "../krogoth_admin/migrations"'
        cmd_n13: str = 'rm -R "../krogoth_apps/migrations"'
        cmd_n14: str = 'rm -R "../krogoth_social/migrations"'
        cmd_n15: str = 'rm -R "../moho_extractor/migrations"'
        cmd_n16: str = 'rm -R "../kbot_lab/migrations"'
        cmd_n18: str = 'docker exec -it armprime ./manage.py makemigrations ' + MAKE_MIGRATIONS
        cmd_n19: str = 'docker exec -it armprime ./manage.py migrate'
        cmd_n21: str = 'docker exec -it armprime ./manage.py installdjangular'


        ORDERED_COMMANDS.append(cmd_n01)
        ORDERED_COMMANDS.append(cmd_n02)
        ORDERED_COMMANDS.append(cmd_n03)
        ORDERED_COMMANDS.append(cmd_n04)
        ORDERED_COMMANDS.append(cmd_n05)
        ORDERED_COMMANDS.append(cmd_n06)
        ORDERED_COMMANDS.append(cmd_n07)
        ORDERED_COMMANDS.append(cmd_n09)
        ORDERED_COMMANDS.append(cmd_n10)
        ORDERED_COMMANDS.append(cmd_n11)
        ORDERED_COMMANDS.append(cmd_n12)
        ORDERED_COMMANDS.append(cmd_n13)
        ORDERED_COMMANDS.append(cmd_n14)
        ORDERED_COMMANDS.append(cmd_n15)
        ORDERED_COMMANDS.append(cmd_n16)
        ORDERED_COMMANDS.append(cmd_n18)
        ORDERED_COMMANDS.append(cmd_n19)
        ORDERED_COMMANDS.append(cmd_n21)


        for cmd in ORDERED_COMMANDS:
            print(bc.green + cmd + bc.ENDC)

        wait = input('ready?')

        os.system('say -v Karen "welcome."')

        installer.destroy_docker()
        installer.execute_realtime_out(cmd_n01, "")

        AKInstallation.execute_realtime_out(cmd_n02, 2)
        AKInstallation.execute_realtime_out(cmd_n03, 3)

        AKInstallation.execute_realtime_out(cmd_n04, 4)
        AKInstallation.execute_realtime_out(cmd_n05, "armprime-redis")

        # CREATE USER 'jawn' with pass: '123123'
        AKInstallation.execute_realtime_out(cmd_n06, 6)
        AKInstallation.execute_realtime_out(cmd_n07, 7)

        ### ---====== remove previous migrations ======---
        AKInstallation.execute_realtime_out(cmd_n09, 9)
        AKInstallation.execute_realtime_out(cmd_n10, 10)
        AKInstallation.execute_realtime_out(cmd_n11, 11)
        AKInstallation.execute_realtime_out(cmd_n12, 12)
        AKInstallation.execute_realtime_out(cmd_n13, 13)
        AKInstallation.execute_realtime_out(cmd_n14, 14)
        AKInstallation.execute_realtime_out(cmd_n15, 15)
        AKInstallation.execute_realtime_out(cmd_n16, 16)

        ### ---====== make new migrations ======---
        AKInstallation.execute_realtime_out(cmd_n18, 17)
        AKInstallation.execute_realtime_out(cmd_n19, 18)

        ### ---====== install krogoth gantry units ======---
        AKInstallation.execute_realtime_out(cmd_n21, 19)

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


InstallationRuntime()