from rest_framework import serializers
from krogoth_gantry.models.core_models import AKFoundationAbstract
from krogoth_gantry.models.models_chat import JawnUser
from krogoth_gantry.models.krogoth_manager import UncommitedSQL
from krogoth_gantry.management.commands.installdjangular import bcolors


class AKFoundationSerializer(serializers.ModelSerializer):
    custom_key_values = serializers.JSONField()

    class Meta:
        model = AKFoundationAbstract
        fields = '__all__'

    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        log_sql = UncommitedSQL(name=instance.unique_name, edited_by=jawn_user, krogoth_class="AKFoundation")
        log_sql.save()
        instance.save()
        return instance

    def create(self, validated_data):
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        log_sql = UncommitedSQL(name=validated_data['unique_name'], edited_by=jawn_user, krogoth_class="AKFoundation")
        log_sql.save()
        return AKFoundationAbstract.objects.create(**validated_data)

