# Django Krogoth
*Copyright (C) 2020 AquaCore*

A Django Project with powerful capabilities out of the box made for rapid single page application development.


![alt text](https://raw.githubusercontent.com/MattAndrzejczuk/Django-Krogoth/master/krogoth.png)

----
## Quickstart On *Ubuntu 16*
### Install Docker
```bash
$ apt-get install -y apt-transport-https 

$ apt-get install -y ca-certificates 
$ apt-get install -y curl 
$ apt-get install -y gnupg-agent 
$ apt-get install -y software-properties-common

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ apt-get update
$ apt-get install docker-ce docker-ce-cli containerd.io
```
----





#### ( **1** ) - Python3 Prerequisits 

`$ sudo apt-get install -y python-pip`

`$ sudo apt-get install -y python3-dev python3-setuptools python3-pip software-properties-common python3-software-properties python3-venv`  

`$ sudo pip3 install --upgrade pip`


#### ( **2** ) - Django Setup

`$ cd krogoth`

`$ python3 -m venv bevn`

`$ source ./bevn/bin/activate`

`$ pip3 install --upgrade pip`

`$ pip3 install -r requirements.txt`

`$ python3 manage.py makemigrations`

`$ python3 manage.py migrate`

`$ python3 manage.py installdjangular`

`$ python3 manage.py collectdvc`

`$ python3 manage.py runserver 0.0.0.0:8000`

## Frontend Development

This app uses AngularJS as the frontend which manages the js files for you automatically.
To write changes to the included components, here's some examples:

 `./manage.py pushup --path "static/web/app/Primary/Required/home/MasterVC/view.html" --name "home" --kind view`

 `./manage.py pushup --path "static/web/app/Primary/Required/home/MasterVC/controller.html" --name "home" --kind controller`

 `./manage.py pushup --path "static/web/app/Directive_Examples/Another_Subcat/Element_With_Events/Directives/movieForm.js" --name "movieForm" --kind directive`

 `./manage.py pushup --path "static/web/app/Directive_Examples/RESTful_Samples/RESTfulModelI/Services/RESTfulModelI.js" --name "RESTfulModelI" --kind service` 



#### Creating New MVC Gantry
```stylus
- [22/Jan/2021 22:10:54] "POST /krogoth_admin/createNewMasterViewController/ HTTP/1.1" 201 20
- [22/Jan/2021 22:10:54] "GET /krogoth_gantry/viewsets/Category/ HTTP/1.1" 200 1412
```

##### TODO: Add These Demos
https://tutorialzine.com/2012/02/apple-like-login-form
https://demo.tutorialzine.com/2012/02/apple-like-login-form/

https://paulrhayes.com/experiments/cube/multiCubes.html
https://github.com/fofr/paulrhayes.com-experiments/blob/master/cube/index.html
