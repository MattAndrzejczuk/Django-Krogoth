#Vanilla ArmPrime 
###No Docker

*For raspberry pi running raspbian*


###### OS SETUP:
```bash
sudo apt-get install -y python3 python3-dev python3-setuptools nginx supervisor postgresql-client
sudo apt-get update
sudo apt-get install -y software-properties-common python3-software-properties
```

###### PYTHON3 SETUP:
```bash
sudo apt-get install python3-venv
pip3 install --upgrade pip
sudo pip3 install -r requirements.txt
```


###### POSTGRESQL SETUP:
```bash
ssh -L 3333:127.0.0.1:<remote mysql port> <username>@<remote host> -N
```

###### POST-INSTALLATION OF ARMPRIME
```bash
pip install django-redis    ///maybe useless
redis-cli config set notify-keyspace-events KEA
sudo -u postgres psql -U postgres postgres -c 'create extension hstore;'
python3 manage.py makemigrations chat krogoth_3rdparty_api krogoth_examples krogoth_apps krogoth_social moho_extractor krogoth_gantry krogoth_core krogoth_admin
python3 manage.py makemigrations
python3 manage.py migrate
```


###### POSTGRESQL SETUP:
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql postgres
\password postgres
```


###### RUN VENV: (optional)
```bash
python3 -m venv ARM_ENV
source ./ARM_ENV/bin/activate
```
