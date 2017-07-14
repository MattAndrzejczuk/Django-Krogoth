# Djangular

## Getting Started

install Docker before you do 'Bootstrap the backend'


## PostgresSQL Console Access:

`$ sudo docker exec -it jawn-postgres bash`

`# su postgres`

`$ psql`


## Bootstrap the backend:

clone to `/home/ubuntu/arm-prime` and run `run-docker-installed.sh`


### Django Administration Guide

Create a new AngularFuseApplication under dynamic_lazarus_page.
Access it via http://127.0.0.1/#!/`FUSE APPLICATION NAME`






# Docker Installation Guide

This is official documentation from Docker Hub simplified.


### 1.) Prepare Ubuntu To Support Docker

`$ sudo apt-get update`

`$ sudo apt-get install apt-transport-https ca-certificates`

`$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D`



### 2.) OPEN UP “/etc/apt/sources.list.d/docker.list”

`$ cd /etc/apt/sources.list.d/`

`$ vi docker.list`



### 3.) PASTE THIS TEXT INTO ‘docker.list’

`deb https://apt.dockerproject.org/repo ubuntu-xenial main`



### 4.) UPDATE APT PACKAGE INDEX

`$ sudo apt-get update`

`$ sudo apt-get install linux-image-extra-$(uname -r)`



### 5.) READY TO INSTALL DOCKER

`$ sudo apt-get install docker-engine`

`$ sudo service docker start`



### 6.) VERIFY DOCKER WORKS

`$ sudo docker run hello-world`




