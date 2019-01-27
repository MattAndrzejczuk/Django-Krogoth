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
os.system(cmd)


OUTPUT_ENABLED = False

def execute(cmd, always_display):
    # out, err = p.communicate()
    os.system(cmd)
    # os.system('clear')
    #if OUTPUT_ENABLED == True or always_display == "NEEDED":
    #    print(out.decode("utf-8"))
    # print(always_display)


print(bc.BOLD + bc.blue + "DESTORYING PREVIOUS KROGOTH " + parent_dir + bc.ENDC + bc.ENDC)
time.sleep(2)

"""
    'docker stop $(docker ps -aq)'
    'echo " ☠️ "'
    'docker rm $(docker ps -aq)'
"""

cmd = ("docker build -t mattjawn/armprime ./app/")
execute(cmd, bc.yellow+"DOCKER BUILD"+bc.ENDC)
db_args = "-e POSTGRES_USER=jawn -d -p 8091:5432 postgres"
db_pw = "58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9"
cmd = ("docker run --name armprime-postgres -e POSTGRES_PASSWORD="+db_pw+" "+ db_args)

execute(cmd, bc.yellow + cmd + bc.ENDC)
cmd = ("docker run -d -p 7070:6379 --name=armprime-redis redis")
execute(cmd, bc.yellow + cmd + bc.ENDC)
cmd = ('docker run -d -p 80:80 -v "'+parent_dir+'":/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime')
execute(cmd, bc.yellow + cmd + bc.ENDC)
#cmd = ('clear')
execute(cmd, bc.yellow + cmd + bc.ENDC)


# print(bc.pink + "INSTALLING KROGOTH: " + parent_dir + bc.ENDC)
# os.system('sh run-docker-installed.sh')

# cmd = ('docker exec -it armprime pip3 install django-redis==4.8.0')
# execute(cmd, bc.purple+"install django-redis"+bc.ENDC)
# cmd = ('docker exec -it armprime apt-get install -y -qq nodejs')
# execute(cmd, bc.purple+"nodejs"+bc.ENDC)
# cmd = ('docker exec -it armprime apt-get install -qq npm')
# execute(cmd, bc.purple+"npm"+bc.ENDC)
# cmd = ('sleep 1')
execute(cmd, bc.lightblue+cmd+bc.ENDC)
cmd = ('docker exec armprime-redis redis-cli config set notify-keyspace-events KEA')
execute(cmd, bc.lightblue+"armprime-redis"+bc.ENDC)
cmd = ("echo 'creating psql extension hstore...'")
execute(cmd, bc.lightblue+"creating psql extension hstore..."+bc.ENDC)
cmd = ('sleep 1')
execute(cmd, bc.lightblue+cmd+bc.ENDC)
# CREATE USER 'jawn' with pass: '123123'
cmd = ('docker exec -it armprime-postgres useradd -p $(openssl passwd -1 123123) jawn')
execute(cmd, bc.lightblue+cmd+bc.ENDC)
cmd = ("docker exec -it --user jawn armprime-postgres psql jawn -c 'create extension hstore;'")
#cmd = ("docker exec -it armprime-postgres psql -U jawn postgres -c 'create extension hstore;'")
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('sleep 1')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../chat/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../krogoth_3rdparty_api/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../krogoth_examples/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../krogoth_admin/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../krogoth_apps/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../krogoth_social/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../moho_extractor/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../kbot_lab/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../LazarusIII/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../LazarusIV/migrations')
# execute(cmd, bc.lightblue+cmd+bc.ENDC)
# cmd = ('rm -R ../LazarusV/migrations')
execute(cmd, bc.lightblue+cmd+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py makemigrations chat krogoth_3rdparty_api krogoth_examples krogoth_apps krogoth_social moho_extractor krogoth_gantry krogoth_core krogoth_admin')
execute(cmd, bc.lightblue+cmd+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py migrate')
execute(cmd, bc.lightgreen+cmd+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py installdjangular')
execute(cmd, bc.lightgreen+cmd+bc.ENDC)
cmd = ('sleep 1')
#execute(cmd, bc.lightgreen+cmd+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py collectstatic')
execute(cmd, bc.lightgreen+"Collecting Static"+bc.ENDC)
cmd = ('docker exec -it armprime ./manage.py collectdvc')
execute(cmd, bc.lightblue+"Installing Default Templates"+bc.ENDC)
cmd = ('sleep 2')
execute(cmd, bc.lightgreen + "INSTALLATION COMPLETED" + bc.ENDC)
execute(cmd, bc.lightgreen + "CREATING SUPER USER: " + bc.ENDC)
os.system('docker exec -it armprime ./manage.py createsuperuser')




print(
    "\n\nTO USE THE PYCHARM DJANGO CONSOLE ON A LOCAL DOCKER CONTAINER, ADD THIS CODE TO THE TOP OF THE STARTING SCRIPT AT: ")
carrot = '\033[91m' + ">" + '\033[0m'
print(
    '\033[36m' + "Preferences " + carrot + " Build, Execution, Deployment " + carrot + "  Console " + carrot + "  Django Console" + '\033[0m')

os.system('sleep 1')
print('\033[95m' + "GENERATED KROGOTH ENVIRONMENT " + '\033[0m')

red = '\033[31m'
ENDC = '\033[0m'
lightblue = '\033[94m'
print('\033[33m' + "\n\nTO USE THE PYCHARM DJANGO CONSOLE, ADD THIS TO THE TOP OF THE STARTING SCRIPT: \n\n\n" + ENDC)
print("import os")
print("os.environ = {}")
for k, v in os.environ.items():
    os.environ[k] = v
    print("os.environ['" + red + k + "", end=(ENDC + "'] = '" + lightblue + v + ENDC + "'\n"))

os.system('sleep 3')
os.system('docker exec -it armprime uwsgi ../runserver_uwsgi.ini')
