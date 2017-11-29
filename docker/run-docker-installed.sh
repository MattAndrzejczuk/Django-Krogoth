#!/bin/bash

dir=$PWD
parentdir="$(dirname "$dir")"
docker build -t mattjawn/armprime ./app/
docker run --name jawn-postgres -e POSTGRES_PASSWORD=58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9 -e POSTGRES_USER=jawn -d postgres
docker run -d -P --name=jawn-redis redis
docker run -d -p 80:80 -v $parentdir:/usr/src/app/ --link jawn-postgres:postgres --link jawn-redis:redis --name=armprime mattjawn/armprime
echo "Running Containers...."
docker exec -it armprime pip3 install jsbeautifier
docker exec -it armprime pip3 install django-dbbackup
docker exec -it armprime pip3 install django-websocket-redis
sleep 3
docker exec -it armprime ./manage.py migrate
docker exec jawn-redis redis-cli config set notify-keyspace-events KEA
echo "Create a Super User"
docker exec -it armprime ./manage.py createsuperuser
echo "Select Yes to Continue Install"
docker exec -it armprime ./manage.py collectstatic
echo "Installing Djangular... "
docker exec -it armprime ./manage.py makemigrations dynamic_lazarus_page Djangular djangular_dashboard
docker exec -it armprime ./manage.py migrate
docker exec -it armprime ./manage.py make_default_layout
##############
# On Mac or Windows with docker-machine installed, remove if Linux ####
# download at: https://docs.docker.com/machine/install-machine/
#echo 'export DOCKER_TLS_VERIFY="1"' >> ~/.bashrc
#echo 'export DOCKER_HOST="tcp://192.168.99.100:2376"' >> ~/.bashrc
#echo 'export DOCKER_CERT_PATH="/Users/dominik/.docker/machine/machines/default"' >> ~/.bashrc
#echo 'export DOCKER_MACHINE_NAME="default"' >> ~/.bashrc
