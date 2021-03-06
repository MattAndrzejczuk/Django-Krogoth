from krogoth_gantry.models.moho_extractor_models import IncludedHtmlMaster, IncludedHtmlCoreTemplate, IncludedJsMaster
from krogoth_gantry.management.commands.installdjangular import bcolors
from krogoth_gantry.functions.edit_mvc import AbstractKrogothSerializer
from krogoth_gantry.models.krogoth_manager import UncommitedSQL
from krogoth_gantry.models.models_chat import JawnUser


class IncludedHtmlMasterSerializer(AbstractKrogothSerializer):
    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=instance.name, edited_by=jawn_user, krogoth_class="IncludedHtmlMaster")
        logThis.save()
        return instance

    def create(self, validated_data):
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=validated_data['name'], edited_by=jawn_user, krogoth_class="IncludedHtmlMaster")
        logThis.save()
        return IncludedHtmlMaster.objects.create(**validated_data)

    class Meta:
        model = IncludedHtmlMaster
        fields = '__all__'


class IncludedJsMasterSerializer(AbstractKrogothSerializer):
    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=instance.name, edited_by=jawn_user, krogoth_class="IncludedJsMaster")
        logThis.save()
        return instance

    def create(self, validated_data):
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=validated_data['name'], edited_by=jawn_user, krogoth_class="IncludedJsMaster")
        logThis.save()
        return IncludedJsMaster.objects.create(**validated_data)

    class Meta:
        model = IncludedJsMaster
        fields = '__all__'


class IncludedHtmlCoreTemplateSerializer(AbstractKrogothSerializer):
    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=validated_data['name'], edited_by=jawn_user, krogoth_class="NgIncludedHtmlCore")
        logThis.save()
        instance.save()
        return instance

    def create(self, validated_data):
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        logThis = UncommitedSQL(name=validated_data['name'], edited_by=jawn_user, krogoth_class="NgIncludedHtmlCore")
        logThis.save()
        return IncludedHtmlCoreTemplate.objects.create(**validated_data)

    class Meta:
        model = IncludedHtmlCoreTemplate
        fields = '__all__'



