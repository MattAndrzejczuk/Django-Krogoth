from rest_framework import serializers
from moho_extractor.models import IncludedHtmlMaster
from krogoth_gantry.management.commands.installdjangular import bcolors
from krogoth_gantry.views import AbstractKrogothSerializer

class IncludedHtmlMasterSerializer(AbstractKrogothSerializer):
    def update(self, instance, validated_data):
        print(bcolors.BOLD + bcolors.lightgreen + "  🛠  " +
              str(type(self)) +
              " \nUPDATED" + bcolors.ENDC + bcolors.ENDC)
        instance.save()
        return instance

    def create(self, validated_data):
        print(bcolors.BOLD + bcolors.TEAL + "  🛠  " +
              str(type(self)) +
              " \nCREATED" + bcolors.ENDC + bcolors.ENDC)
        return IncludedHtmlMaster.objects.create(**validated_data)

    class Meta:
        model = IncludedHtmlMaster
        fields = '__all__'