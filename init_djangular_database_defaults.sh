#!/bin/bash

echo 'Djangular - Copyright Matt Andrzejczuk 2017'
echo ''
echo 'Initializing Database for the first time.'
echo ''

python3 manage.py makemigrations dynamic_lazarus_page GeneralWebsiteInfo DatabaseSandbox LazarusII LazarusDatabase Djangular rest_auth
python3 manage.py migrate

