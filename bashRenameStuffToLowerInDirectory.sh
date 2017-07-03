#!/bin/bash


find '/usr/src/app/static/mods/'$1 -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;

