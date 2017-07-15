#!/bin/bash
#echo "Installing docker...."
#apt-get update
#apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
#apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
#apt-get update
#apt-get install -y docker-engine
#echo "Setting up 3 Docker Containers...."
dir=$PWD
parentdir="$(dirname "$dir")"
docker build -t jawn ./app/
docker run --name jawn-postgres -e POSTGRES_PASSWORD=58bdf87d93a3f325574900aa2f5626e3844a903ffb64bed152ae124d2e79aab9 -e POSTGRES_USER=jawn -d postgres
docker run -d -P --name=jawn-redis redis
docker run -d -p 80:80 -v $parentdir:/usr/src/app/ --link jawn-postgres:postgres --link jawn-redis:redis --name=jawn jawn
echo "Running Containers...."
docker exec -it jawn pip3 install jsbeautifier
docker exec -it jawn pip3 install django-dbbackup
sleep 3
docker exec -it jawn ./manage.py migrate
docker exec jawn-redis redis-cli config set notify-keyspace-events KEA
echo "Create a Super User"
docker exec -it jawn ./manage.py createsuperuser
echo "Select Yes to Continue Install"
docker exec -it jawn ./manage.py collectstatic
##############
# On Mac or Windows with docker-machine installed, remove if Linux ####
# download at: https://docs.docker.com/machine/install-machine/
#echo 'export DOCKER_TLS_VERIFY="1"' >> ~/.bashrc
#echo 'export DOCKER_HOST="tcp://192.168.99.100:2376"' >> ~/.bashrc
#echo 'export DOCKER_CERT_PATH="/Users/dominik/.docker/machine/machines/default"' >> ~/.bashrc
#echo 'export DOCKER_MACHINE_NAME="default"' >> ~/.bashrc
