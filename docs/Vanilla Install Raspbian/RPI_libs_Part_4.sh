pip3 install psycopg2 
pip3 install psutil
apt install postgresql postgresql-contrib
-u postgres createuser --interactive
adduser romulus
-u romulus createdb romulus
-u romulus psql romulus -c 'create extension hstore;'
-u romulus psql romulus -c '\password'
