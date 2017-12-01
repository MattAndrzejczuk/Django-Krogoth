#!/bin/bash


find $1 -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;

