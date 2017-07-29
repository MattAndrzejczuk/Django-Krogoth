# Djangular


# Django, uWSGI and Nginx in a container

This Dockerfile allows you to build a Docker container with a fairly standard
and speedy setup for Django with uWSGI and Nginx.

uWSGI from a number of benchmarks has shown to be the fastest server 
for python applications and allows lots of flexibility.

Nginx has become the standard for serving up web applications and has the 
additional benefit that it can talk to uWSGI using the uWSGI protocol, further
elinimating overhead. 

Most of this setup comes from the excellent tutorial on 
https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html

Feel free to clone this and modify it to your liking. And feel free to 
contribute patches.

### Build and run
* docker build -t webapp .
* docker run -d webapp

### How to insert your application

In /app currently a django project is created with startproject. You will
probably want to replace the content of /app with the root of your django
project.

uWSGI chdirs to /app so in uwsgi.ini you will need to make sure the python path
to the wsgi.py file is relative to that.



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






# How To Install Docker On Ubuntu
##### should be fine on any other linux distro

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




