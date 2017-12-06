#!/bin/bash


#~~~ This part requires:
#~~~ $ sudo apt-get install Xvfb
#~~~ $ Xvfb :0 -screen 0 640x480x8 &




# HPIPack [-d DirectoryToPack] [-f HPIFileName] [auto]

DISPLAY=:0 wine '/usr/src/app/static/HPI_Tools/HPIPack.exe' -d $1 -f $2 auto






# THIS ONE WORKED WELL:
#DISPLAY=:0 wine32 explorer /desktop=name,640x480 HPIPack.exe -d UnitsToPack -f CompressedFile.CCX auto