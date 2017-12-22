#!/bin/bash

dir=$PWD
parentdir="$(dirname "$dir")"


echo "\033[1;31mKROGOTH v0.6.98"
echo "Copyright (C) 2017 Matt Andrzejczuk < matt@jawn.it >\033[0m"
echo "\033[1;32mKROGOTH can not be copied and/or distributed without the express permission of Matt Andrzejczuk.\033[0m"
sleep 3

docker build -t mattjawn/armprime ./app/
docker run --name armprime-postgres -e POSTGRES_PASSWORD=58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9 -e POSTGRES_USER=jawn -d -p 8091:5432 postgres
docker run -d -P --name=armprime-redis redis
docker run -d -p 80:80 -v $parentdir:/usr/src/app/ --link armprime-postgres:postgres --link armprime-redis:redis --name=armprime mattjawn/armprime
echo "\033[1;36mRunning Containers....\033[0m"
docker exec -it armprime pip3 install django-redis==4.8.0
#docker exec -it armprime pip3 install django-dbbackup
#docker exec -it armprime pip3 install django-websocket-redis
#docker exec -it armprime pip3 install fcm-django==0.2.12
sleep 1
docker exec -it armprime ./manage.py makemigrations
sleep 1
docker exec -it armprime ./manage.py migrate
docker exec armprime-redis redis-cli config set notify-keyspace-events KEA
echo "\033[1;36mCreate a Super User\033[0m"
docker exec -it armprime ./manage.py createsuperuser
echo "\033[1;36mSelect Yes to Continue Install\033[0m"
docker exec -it armprime ./manage.py collectstatic
echo "\033[1;36mInstalling krogoth_gantry... \033[0m"
docker exec -it armprime ./manage.py makemigrations moho_extractor krogoth_gantry djangular_dashboard LazarusIV LazarusV chat
docker exec -it armprime ./manage.py migrate
docker exec -it armprime ./manage.py make_default_layout
echo "\033[1;34m NOW SERVING KROGOTH, IT WILL BE AVAILABLE ON: \033[0m"
echo "\033[4;36m http://127.0.0.1 \033[0m"
echo "\033[1;35m"
docker exec -it armprime uwsgi ../runserver_uwsgi.ini
##############
# On Mac or Windows with docker-machine installed, remove if Linux ####
# download at: https://docs.docker.com/machine/install-machine/
#echo 'export DOCKER_TLS_VERIFY="1"' >> ~/.bashrc
#echo 'export DOCKER_HOST="tcp://192.168.99.100:2376"' >> ~/.bashrc
#echo 'export DOCKER_CERT_PATH="/Users/dominik/.docker/machine/machines/default"' >> ~/.bashrc
#echo 'export DOCKER_MACHINE_NAME="default"' >> ~/.bashrc

sleep 1
echo ""
echo "Installing Wine for Microsoft Windows applications compatibility."
sleep 3
docker exec -it armprime bash -c "add-apt-repository -y ppa:ubuntu-wine/ppa"
docker exec -it armprime bash -c "apt-get update"
docker exec -it armprime bash -c "apt-get install -y wine"
docker exec -it armprime bash -c "dpkg --add-architecture i386"
docker exec -it armprime bash -c "apt-get update"
docker exec -it armprime bash -c "apt-get install wine32"
docker exec -it armprime bash -c "apt-get install Xvfb"
docker exec -it armprime bash -c "Xvfb :0 -screen 0 640x480x8 &"
sleep 1
echo ""
echo "Wine Installation: "
docker exec -it armprime bash -c "wine --version"
sleep 2
echo ""
echo "DONT FORGET TO RUN THIS IN POSTGRESQL ! ! ! ! "
echo "psql jawn4 -c 'create extension hstore;'"
echo " "