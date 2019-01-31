#!/usr/bin/env bash



echo "  ☠️  WARNING ☠️  "
#echo "Stop and remove all running containers? (y/n)"
#read answer
#if echo "$answer" | grep -iq "^y" ;then
#    python -c 'print(" \033[33m Whaling in progress... \033[0m ")'
#    docker stop armprime-redis
#    python -c 'print(" \033[31m TERMINATED redis \033[0m ")'
#    docker stop armprime-postgres
#    python -c 'print(" \033[32m TERMINATED postgres \033[0m ")'
#    docker stop armprime
#    python -c 'print(" \033[34m TERMINATED django \033[0m ")'
#    docker rm armprime-redis
#    python -c 'print(" \033[31m DESTROYED redis \033[0m ")'
#    docker rm armprime-postgres
#    python -c 'print(" \033[32m DESTROYED redis \033[0m ")'
#    docker rm armprime
#    python -c 'print(" \033[34m DESTROYED django \033[0m ")'
#    python -c 'print(" \033[33m Recycling whale blubber... \033[0m ")'
#else
#    echo "Cancelled."
#fi


echo "Stop and remove all running containers? (y/n)"
read answer
if echo "$answer" | grep -iq "^y" ;then
    docker stop $(docker ps -aq)
    python -c 'print(" \033[32m TERMINATED. \033[0m ")'
    docker rm $(docker ps -aq)
    python -c 'print(" \033[32m DESTROYED. \033[0m ")'
else
    echo "Cancelled."
fi