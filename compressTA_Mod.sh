#!/bin/bash


# HPIPack [-d DirectoryToPack] [-f HPIFileName] [auto]

DISPLAY=:0 wine '/usr/src/app/static/HPI_Tools/HPIPack.exe' -d $1 -f $2 auto
