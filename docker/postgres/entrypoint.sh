#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "rcrf" <<-EOSQL
    CREATE USER rcrf2;
    CREATE DATABASE rcrf2;
    GRANT ALL PRIVILEGES ON DATABASE rcrf2 TO rcrf2;
EOSQL