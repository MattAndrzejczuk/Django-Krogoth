#!/bin/bash


#~~~ This part requires:
#~~~ $ sudo apt-get install Xvfb
#~~~ $ Xvfb :0 -screen 0 1024x768x16 &




# HPIPack [-d DirectoryToPack] [-f HPIFileName] [auto]

DISPLAY=:0 wine '/usr/src/app/static/HPI_Tools/HPIPack.exe' -d $1 -f $2 auto
