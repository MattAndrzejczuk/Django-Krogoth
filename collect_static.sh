#!/bin/bash

docker exec -it jawn ./manage.py collectstatic --no-input

