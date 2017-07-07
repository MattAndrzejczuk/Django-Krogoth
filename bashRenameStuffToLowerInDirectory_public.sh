#!/bin/bash


find '/usr/src/persistent/media/ta_data/'$1 -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;

