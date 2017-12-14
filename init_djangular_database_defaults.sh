#!/bin/bash

echo 'krogoth_gantry - Copyright Matt Andrzejczuk 2017'
echo ''
echo 'Initializing Database for the first time.'
echo ''

python3 manage.py makemigrations moho_extractor GeneralWebsiteInfo DatabaseSandbox LazarusII LazarusDatabase krogoth_gantry rest_auth
python3 manage.py migrate

