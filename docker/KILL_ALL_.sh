


echo "  ☠️  ☠️  ☠️  ☠️  ⚠️  WARNING ! ! !"


echo "Stop and remove all running containers? (y/n)"
read answer
if echo "$answer" | grep -iq "^y" ;then
    echo " 🛑 "
    docker stop $(docker ps -aq)
    echo " ☠️ "
    docker rm $(docker ps -aq)
else
    echo "Cancelled."
fi


#docker stop $(docker ps -aq)
#docker rm $(docker ps -aq)
