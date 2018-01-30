echo "☢ ☢ ☢ WARNING ☢ ☢ ☢"
echo "This will permanently wipe out ALL migrations, continue? (y/n)"
read answer
if echo "$answer" | grep -iq "^y" ;then
    echo " ☢ ☢ NUCLEAR LAUNCH DETECTED ☢ ☢ "
    rm -R ../chat/migrations
    rm -R ../krogoth_3rdparty_api/migrations
#    rm -R ../krogoth_gantry/migrations
    rm -R ../krogoth_examples/migrations
#    rm -R ../krogoth_core/migrations
    rm -R ../krogoth_apps/migrations
    rm -R ../krogoth_social/migrations
    rm -R ../moho_extractor/migrations
    rm -R ../kbot_lab/migrations
    rm -R ../LazarusIII/migrations
    rm -R ../LazarusIV/migrations
    rm -R ../LazarusV/migrations
    sleep 1
    reset
else
    echo "Cancelled."
fi


#docker stop $(docker ps -aq)
#docker rm $(docker ps -aq)
