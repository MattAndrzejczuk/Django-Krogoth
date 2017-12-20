#!/bin/bash
# bash extractTA_Mod.sh 'CiniCraft/UFO_FILE_1.ufo' 'CiniCraft/UFO_FILE_1/'

echo Getting started
echo $1
echo $2
echo


echo HPIDump 1.5.1 - HPI File Extract
echo
echo Credits:
echo Eric DeZert for writing WriteHPI.
echo ZLib compression and decompression by Jean-loup Gailly: compression
echo Mark Adler: decompression
echo For more info, see the zlib Home Page at http://www.cdrom.com/pub/infozip/zlib/


echo Implemented into Total Annihilation: Lazarus by Matt Andrzejczuk
echo July 7th 2017
echo
sleep 0.2s

## EXTRACT A BUNCH FROM SINGLE DIRECTORY:
## for f in /usr/src/app/static/mod1_ufos/UnitsToPack/*;

wine /usr/src/app/static/HPI_Tools/HPIDump.exe $1 -o $2;



