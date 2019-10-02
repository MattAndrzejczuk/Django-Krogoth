# Krogoth

> Version 0.9.x, September 2019

> Copyright (C) 2019 Gantry




## Quickstart On *Ubuntu 18.04* With Docker
> Last Updated: October 1st, 2019 

For simplicity, this guide will use a vanilla Ubuntu 18.04 droplet from Digital Ocean.

1. Clone the repo:

    `root@ubuntu:~# git clone git@bitbucket.org:cinicraft/krogoth.git`

2. Update packages:

    `root@ubuntu:~# apt-get update`

3. Remove old versions of docker:

    `apt-get remove docker docker-engine docker.io`

4. Install docker:

    `apt install docker.io`
    
5. (optional) automatically have docker run during OS startup: 

    `sudo systemctl start docker`
    
    `sudo systemctl enable docker`

6. Navigate to the docker directory

    `cd docker`
    
7. Run the installer, follow on screen instructions. (installation may take awhile)

    `cd docker`
    
#
#
#
## Manual Installation on *Ubuntu 18.04*
> Last Updated: January 16th, 2019 


#### Prerequisits
```bash
apt-get install -y python3 python3-dev python3-setuptools \ 
    nginx supervisor postgresql-client 
    
apt-get install -y build-essential git libpq-dev sqlite3 build-essential git \
    software-properties-common python3-software-properties python3-pip
apt-get update

rm -rf /var/lib/apt/lists/*
```


```bash
pip3 install --upgrade pip
pip3 install uwsgi
```


#### 
```bash
mkdir -p /usr/src/app
mkdir -p /usr/src/volatile/static
mkdir -p /usr/src/persistent/media

git clone https://cinicraft@bitbucket.org/cinicraft/arm-prime.git
cp -R arm-prime/* /usr/src/app/.
```

## Preparing NGINX

```bash

add-apt-repository -y ppa:nginx/stable
echo "daemon off;" >> /etc/nginx/nginx.conf
export DJANGO_SETTINGS_MODULE="rcrfbackend.settings"
rm /etc/nginx/sites-enabled/default
ln -s /usr/src/nginx-app.conf /etc/nginx/sites-enabled/
ln -s /usr/src/supervisor-app.conf /etc/supervisor/conf.d/
pip3 install -r /usr/src/app/requirements.txt 
supervisord 
```



---

#The Purpose of Krogoth
AngularJS began with a bright and exciting future since its release in the early 2010s.
But as time went on, its performance issues, steep learning curve, and two way data binding problems began to surface.
The future of AngularJS looked bleak with the announcement of Angular 2. Angular2 doesn't work with AngularJS, and if 
learning AngularJS was hard enough, Angular2 requires for you to take up learning TypeScript. TypeScript doesn't even 
execute when run on many browsers, so you'll also need to figure out how to even get started with a new project and get 
the damn thing to compile back to JavaScript. If that's not frustrating enough, Angular 4 no longer uses TypeScript and 
has yet again altered the programming language needed to run the framework.
So what are we to do here? Skip Angular 2 and go straight over to 4? What if we just finished mastering the enigmatic 
AngularJS directives, and services. Is it worth it spending the next six months burning the midnight oil to master the 
same thing again? Will Angular 4 amaze me the same way AngularJS did when I discovered features like form validators, 
impressive and recyclable animations you can throw into your search input element that took you less than 30 minutes to 
get working? I'm pretty skeptical about making the switch, and the benefits of upgrading to Angular 4 don't seem to be 
outweighing the cost of time you'll need to spend learning it. This is where Krogoth for Django comes in.
Django's server side template engine was pretty incredible to me when I first got a good understanding of how to use it. 
And it was especially powerful when mixed properly with jQuery. Being able to use Python as a replacement for JavaScript 
in certain situations was a very welcoming concept. So why add another front end, superset like TypeScript to clean up 
and fix the issues that have plagued AngularJS when you could just use something more preferable like Python instead? 
JavaScript is the language developers love to hate, there's no reason to abandon AngularJS and throw the baby out with 
the bath water. AngularJS was created for developers accustomed to Java, C# and all other object oriented programming 
languages so we could finally treat JavaScript as such. While critics of AngularJS scoff at the difficultly of learning 
how to use directives, services and factories, they should ask themselves. Do you write your C++ in notepad? Or do you 
just write entire x86 and x64 apps in pure assembly language? Of course not, chances are, you use visual studio or Xcode 
that handle a ton of minor details for you so you can quickly build and compile your app. This is what Krogoth 
fundamentally is. You can continue writing your AngularJS app just like you've always done before, and let the Krogoth 
compiler handle setting up the services and directives for you.


#Krogoth For Production Environments
Krogoth in its current state is not ready for production. This is mainly because the AngularJS front end does not yet 
compile into static files, this will change in the near future. Most of its JS, CSS, and HTML files are served directly 
from SQL as of now, which can easily be changed later by dumping the contents of SQL into a static directory. These 
static files can be read later by using an altered version of the index.html file to read from the new static source. 
This update should be completed soon, since the Django views responsible for serving JS and HTML files from SQL only make  
slight changes to these front end files, and a new mechanism will need to be added that simply replicates these adjustments 
before saving them into a static directory which will allow you to serve your Krogoth views, controllers, directives and 
services from multiple light weight NGINX servers.


#Getting Started

###Before You Clone Krogoth
Docker is required for Krogoth to install and run, follow the steps below for your OS to get Docker up and running.
####CentOS 7 64-bit
Add docker repo for the yum package manager:
```bash
    $ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```
```bash
    $ sudo yum install docker-ce
```
```bash
    $ sudo systemctl start docker
```


####Ubuntu 16.04 64-bit
```bash
    $ sudo apt install curl
```

```bash
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```bash
    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

```bash
    $ sudo apt-get update
```

```bash
    $ apt-cache policy docker-ce
```

```bash
    $ sudo apt-get install -y docker-ce
```




#####Verify Successful Docker Installation
```bash
    $ sudo docker run hello-world
```






Krogoth is intended to be used by anyone from all skill levels from students to seniors. I had originally developed 
Krogoth as a way to quickly deploy a monolithic Django app for blogging, but found that it takes too much time to go 
through the process of integrating an off the shelf AngularJS template into a fresh new Django project. This is the 
reason why Krogoth's only prerequisite is Docker CE to be installed on any x64-bit Linux machine. You should be able to 
get Krogoth up and running by simply running the following bash command:
```bash
    $ sudo sh run-docker-installed.sh
```

The installation can take anywhere from 15 to 30 minutes depending on your internet connection speed. Once the 
installation completes, you should be able to navigate to your localhost:80 and see that your Krogoth installation had 
succeeded with a screen that says **it works!**.

---

#Creating Your First Krogoth Component
By now your Krogoth web server should be up and running. You are now ready to start creating states for your single 
paged web application. Since Krogoth is intended to always operate as a single paged web application, your users will 
no longer be reloading entire web pages as they navigate and explore your site. Instead of web pages, Krogoth allows its 
users to navigate your website through states.

######Worry Less About Separation of Concerns

AngularJS alone made the process of creating states very difficult, even if developers wanted to simply create an 
**About Me** page or **Contact Us** page, there was a lot of room for error especially for beginners. If just one string 
is misspelled for a new and simple **Contact Us** page, a very vague error message will be thrown, and the entire app 
itself will crash.  The difficulty and separation of concerns issue in AngularJS alone is one of the main reasons why 
Angular 2 and Vue.js gained so much momentum ever since both frameworks were released.
##Krogoth Makes It Easy
With Krogoth, you can add entire Controllers, Directives, Services and Factories within seconds. When you begin creating 
one of these 4 AngularJS components, a default scaffold is generated for you. So if you're new to factories and 
directives, you can create a blank default component with the included default scaffold and see for yourself how they 
work. Many beginner AngularJS developers usually avoid working with directives and services because of how complicated 
and enigmatic they are, not anymore with Krogoth. Finally beginners will be able to step outside of their comfort zones 
and witness the true power of pure JavaScript.


######A Collection of Experimental Sample Templates
Included within the Krogoth Gantry section of the Django admin panel is a collection of directives and services that'll 
push your web browser and web client hardware to its limits. Some of these examples include:

;
* 4K Gaussian Blur Frosted Glass Background
* 3D Model Viewer
* Web Socket Component
* 2D Canvas Rendering The Golden Ratio in Real-Time



These experimental samples will drain any computer system's hardware, but regardless of the amount of processing power they 
consume, they remain encapsulated within their own MasterViewControllers. We look forward to the community taking these 
examples to create more next generation directives and services that are more efficient and further blur the line 
between native and web applications.

---

#Problems With AngularJS Solved With Krogoth
###Lazy Loading
* Don't load controllers, services, nor directives until the user explicitly requests the parent Master View Controller.
###Dynamic Loading
* Kill and reload controllers
###Code Organization
* Managed automatically by SQL and Django Administration
###Onboarding Team Members
* New blood will only need to know pure JS
###Two-way data-binding
* Use the vm design pattern
###Dependency Injection
* Clean and makes perfect sense thanks to Django and SQL.
###Inherited Variables Are Global Variables
* Dangerous, from child scope you can access absolutely any variable of any parent scope. Krogoth allows you to easily 
create non-global factories and directives which are only accessible to their parent component along with the parent's 
children.
###Search Engine Optimization 
* Since Krogoth manages and organizes your single page application states, it can also take care of your SEO, by 
automatically generated site maps to ensure any web crawlers, both old and new can find the exact content the world is 
looking for.



##Edit Changes To The Frontend Anywhere & Anytime With A Browser Based IDE
For developers that need to meet deadlines, a quick and easy method for writing RESTful APIs is a must have. And 
constantly editing and re-uploading static files can add hours over the course of a week of development. Krogoth can cut 
hours out of the development and testing of complex Ajax request made to the server thanks to the two built-in IDEs.


######The Django Admin Panel IDE
The first IDE is the simplest one which lives inside the Django admin panel. This IDE contains less features for coding 
but gets developers new to Krogoth more familiar with the overall underpinnings of how Krogoth works. If you're very 
familiar and comfortable with Django applications, then the IDE within the admin panel is the best place to start 
familiarizing yourself with Krogoth and the way it fuses together Django and AngularJS into a single full stack. It will 
also give you a better idea of exporting the front end code into static files which could then be used in a production 
environment like a light weight NGINX server which would only be responsible for serving raw static files compiled by 
Krogoth. For developers who've worked with or are familiar with Drupal or Wordpress and the way they store HTML and JS 
code in a SQL server to then be displayed using PHP, should have a pretty good idea of how Krogoth works.


######The Pure AngularJS IDE
This IDE is the better one since it functions purely as a standalone view. The pure AngularJS IDE works better since 
saving and loading Krogoth components is handled via Ajax requests, which allows you to load and save documents without 
reloading or refreshing the browser since it also functions as a single paged app. The Django Admin IDE is limited in 
functionality since it lives alongside pre-existing Django/Python code and uses the older jQuery library.



##AngularJS may be a resource hog, but JavaScript cheated the death of Moore's Law
JavaScript can be a headache sometimes, but this is because of its asynchronous nature. Due to this asynchronous factor, 
it has turned a language that was originally created as a toy programing language into a sleeping giant. When the intel 
Pentium 4 was released in the early 2000s, the speed of individual CPU processors would barely be improved upon up until 
today in 2018 where overclocking is required to barely scratch the surface of 5GHz on a high-end intel chip, 
but we have seen a dramatic increase in the amount of processor cores that provide huge performance benefits to 
multithreaded apps written in technologies like JavaScript. Since 2014 when AngularJS became a hit, the amount CPU cores 
on both desktops and mobile devices has doubled, with affordable hexacore desktop processors already available for older 
Socket types on the market and the recently launched product line of Core i9 processors by intel with hexacore 
processors.



##Search Engine Optimization
A feature which will be released soon, Krogoth will handle SEO for you automatically by scouring through all of your 
public states, both master and slave, to then generate a downloadable XML site map for web crawlers to analyze. This was 
originally a limitation for AngularJS since single paged web applications must be indexed in a certain way, and 
generating an extra site map will help those crawlers explore your Krogoth app's content. The site map lives in the 
primary index.html page within the HEAD tag.



##RESTful API Development
With Krogoth, many example API scaffolds are included out of the box complete with samples ranging from single property 
models to complex models with multiple relations with other models. The models included are also pre-integrated with the 
AngularJS front end, along with elegant and clean code implementations that match up with the latest in quality 
standards. So you'll spend more time visualizing and organizing your brand and inventory rather than spending hours of 
time with development and testing.



---



#It Just Works, Right Out of The Box

Krogoth, like Django will be optimized for perfectionists with deadlines. The only thing you need to get Krogoth up and 
ready for business on your website is Docker CE preinstalled on the 64 bit OS of your choice. Simply clone, install, and 
start development right away. 


###Fast & Easy Method For Tweaking & Testing Your Installer
####Undo all changes properly for git clone
Freshly cloned Krogoth projects will generate many files after installation which may confuse git.
If you know for a fact that your Krogoth local repository doesn't have any unsaved changes and you'd simply like to
pull the latest changes for the purpose of applying a hotfix to your installation process, the following git commands
will help you restore Krogoth into a fresh state in a situation where you are working on the installation process.

__THIS WILL DELETE ALL OF YOUR UNCOMMITED WORK, PROCEED WITH CAUTION__
```bash
    $ git clean -f
    $ git reset --hard
    $ git pull
```

As you make changes to your installer scripts such as **run-docker-installed.sh**, you will need a quick way to wipe
and pull the latest changes on your testing server. The command lines above will reset your repository into a fresh
and never removed from box state which will allow you to check and see if the latest commit fails on installation.
This is useful in a situation where you have a new developer join your team, and you'd like to help get them up and 
running with a testing server using a freshly installed virtual machine running Ubuntu. One of the cornerstones of 
Krogoth is the ability to become fully operational using few enough commands you could count using one hand.







[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/1PwiljBN5-8/0.jpg)](https://www.youtube.com/watch?v=1PwiljBN5-8)

[Your Krogoth project should never be PC](http://www.youtube.com/watch?v=1PwiljBN5-8)


---


# Using bower with Krogoth (ALPHA)

Eventually there will be more simple and seamless compatibility with legacy package managers like bower and npm.
For now, here's how you can use bower alongside Krogoth and simplify the installation of your app's dependencies.


### 1.) Install your AngularJS package
```bash
    $ bower install ng-websocket
```

If you receive this error:
    /usr/bin/env: ‘node’: No such file or directory
    
Then do the following:
```bash
    $ sudo ln -s /usr/bin/nodejs /usr/bin/node
```

### 2.) update your index.module import dependency
* navigate to http://localhost/admin_a9k/krogoth_core/akfoundationangularcore/
* open **module.core** under Home » Krogoth_Core » Core Application
* add your dependency declaration
```javascript
'use strict';
angular.module('app.core', ['ngWebsocket']);
```

### 3.) make sure you add the path to this bower package to your __index.html__ file:
```html
<script src="/static/bower_components/ng-websocket/ng-websocket.js"></script>
```


---


#####Questions?
Contact me at: **<**matt@jawn.it**>**
