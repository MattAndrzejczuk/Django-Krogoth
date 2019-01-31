from rest_framework import serializers
from krogoth_core.models import AKFoundationAbstract
from krogoth_chat.models import JawnUser
from krogoth_admin.models import UncommitedSQL
from krogoth_gantry.management.commands.installdjangular import bcolors


class AKFoundationSerializer(serializers.ModelSerializer):
    custom_key_values = serializers.JSONField()
    #    class Meta:
    #        model = AKFoundationAbstract
    #        fields = '__all__'
    class Meta:
        model = AKFoundationAbstract
        fields = '__all__'

    def update(self, instance, validated_data):
        print(bcolors.BOLD + bcolors.lightgreen + "  🛠  " +
              str(type(self)) +
              " \nUPDATED" + bcolors.ENDC + bcolors.ENDC)
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=instance.unique_name, edited_by=jawn_user, krogoth_class="NgIncludedHtml")
        logThis.save()
        instance.save()
        return instance

    def create(self, validated_data):
        print(bcolors.BOLD + bcolors.TEAL + "  🛠  " +
              str(type(self)) +
              " \nCREATED" + bcolors.ENDC + bcolors.ENDC)
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=instance.unique_name, edited_by=jawn_user, krogoth_class="NgIncludedHtml")
        logThis.save()
        return AKFoundationAbstract.objects.create(**validated_data)

