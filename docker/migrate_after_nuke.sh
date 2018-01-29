docker exec -it armprime ./manage.py makemigrations chat krogoth_3rdparty_api krogoth_gantry krogoth_examples krogoth_core krogoth_apps krogoth_social moho_extractor
docker exec -it armprime ./manage.py migrate


echo "You will need to add these to core and gantry krogoth apps:"
echo " ...  "
echo "from django.contrib.postgres.operations import HStoreExtension"
echo "docker exec -it armprime ./manage.py migrate"