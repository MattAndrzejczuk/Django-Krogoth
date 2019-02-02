#!/usr/bin/env bash


# REVERT OR FASTFORWARD TO THE LATEST master COMMIT.
# use this for clean project recloning


echo "  ☠️  \033[91m DANGER ZONE \033[0m ☠️  "
sleep(1)
echo "\033[93m By entering 'y', this krogoth unit will be reverted to the latest master branch. \033[0m"
echo "\033[93m Any unsaved or uncommited progress will be lost. \033[0m"
sleep(2)
echo "\033[31m CONTINUE? \033[0m"

echo "\033[90m (y) (n) \033[0m"



read answer
if echo "$answer" | grep -iq "^y" ;then
    git clean -f
    git reset --hard
    git pull
else
    echo "Cancelled."
fi