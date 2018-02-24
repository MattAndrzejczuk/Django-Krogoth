#!/bin/bash

dir=$PWD
parentdir="$(dirname "$dir")"

reset

v1="\033[92m"
v2="KROGOTH v0.8.20"
v3="\033[;0m\033[93m"

v4="Copyright (C) 2017 Matt Andrzejczuk <\033[;0m"
v5="\033[36m"
v6="matt@jawn.it"
v7="\033[31m"
v8="\033[93m>\033[93m"

v9="\033[95m"
v10="KROGOTH can not be copied and/or distributed without the express permission of Matt Andrzejczuk."
v11="\033[;0m"

p1=$v1$v2$v3
p2=$v4$v5$v6$v7$v8
p3=$v9$v10$v11

echo $p1
echo $p2
echo $p3

sleep 2

docker build -t mattjawn/armprime ./app/
echo "  💦 armprime "
docker run --name armprime-postgres -e POSTGRES_PASSWORD=58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9 -e POSTGRES_USER=jawn -d -p 8091:5432 postgres
echo "  💦 armprime-postgres "
docker run -d -P --name=armprime-redis redis
echo "  💦 armprime-redis "
docker run -d -p 80:80 -v $parentdir:/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime
echo "\033[1;36mRunning Containers....\033[0m"

docker exec -it armprime pip3 install django-redis==4.8.0
docker exec -it armprime apt-get install -y -qq nodejs
docker exec -it armprime apt-get install -qq npm

sleep 1

docker exec armprime-redis redis-cli config set notify-keyspace-events KEA

echo '\033[33m'
echo 'creating psql extension hstore...'
echo "\033[0m"
sleep 1
docker exec -it --user postgres armprime-postgres psql jawn -c 'create extension hstore;'
sleep 1

rm -R ../chat/migrations
rm -R ../krogoth_3rdparty_api/migrations
# rm -R ../krogoth_gantry/migrations
rm -R ../krogoth_examples/migrations
# rm -R ../krogoth_core/migrations
rm -R ../krogoth_apps/migrations
rm -R ../krogoth_social/migrations
rm -R ../moho_extractor/migrations
rm -R ../kbot_lab/migrations
rm -R ../LazarusIII/migrations
rm -R ../LazarusIV/migrations
rm -R ../LazarusV/migrations

docker exec -it armprime ./manage.py makemigrations chat krogoth_3rdparty_api krogoth_examples krogoth_apps krogoth_social moho_extractor krogoth_gantry krogoth_core
docker exec -it armprime ./manage.py migrate
docker exec -it armprime ./manage.py installdjangular

sleep 1
echo '\033[33m'
docker exec -it armprime ./manage.py createsuperuser
echo "\033[0m"
echo "\033[35m"
docker exec -it armprime ./manage.py collectstatic
echo "\033[0m"
echo '\033[34m'
docker exec -it armprime ./manage.py collectdvc
echo "\033[0m"
echo '\033[32m'
docker exec -it armprime uwsgi ../runserver_uwsgi.ini
echo "\033[0m"



##############
# On Mac or Windows with docker-machine installed, remove if Linux ####
# download at: https://docs.docker.com/machine/install-machine/
#echo 'export DOCKER_TLS_VERIFY="1"' >> ~/.bashrc
#echo 'export DOCKER_HOST="tcp://192.168.99.100:2376"' >> ~/.bashrc
#echo 'export DOCKER_CERT_PATH="/Users/dominik/.docker/machine/machines/default"' >> ~/.bashrc
#echo 'export DOCKER_MACHINE_NAME="default"' >> ~/.bashrc
#   cyan = '\033[36m'
#    lightgrey = '\033[37m'
#    darkgrey = '\033[90m'
#    lightred = '\033[91m'
#    lightgreen = '\033[92m'
#    yellow = '\033[93m'
#    lightblue = '\033[94m'
#    pink = '\033[95m'
#    lightcyan = '\033[96m'