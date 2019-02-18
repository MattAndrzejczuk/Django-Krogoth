from rest_framework import serializers
from krogoth_admin.models import UncommitedSQL
from krogoth_gantry.models import KrogothGantrySlaveViewController, \
    KrogothGantryCategory, KrogothGantryMasterViewController, KrogothGantryDirective, \
    KrogothGantryService, AKGantryMasterViewController
from jawn.settings import BASE_DIR
from krogoth_chat.models import JawnUser
from krogoth_gantry.helpers.os_directory import MoveToNewDirectory
from krogoth_gantry.management.commands.installdjangular import bcolors




class AbstractKrogothSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
            print(bcolors.BOLD + bcolors.blue + "  🛠  " +
                  str(type(self)) + " : " + str(key) +
                  " \nUPDATED" + bcolors.ENDC + bcolors.ENDC)
        instance.save()
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        uncommitedChange = UncommitedSQL.objects.create(name=instance.name,
                                                        edited_by=jawn_user,
                                                        krogoth_class="KrogothGantryMasterViewController")
        return instance

    ### To do later, recycle reflection from class "krogoth_gantryModelForm"
    ### too much going on in this .py file now.
    def create(self, validated_data):
        print(bcolors.BOLD + bcolors.purple + "  🛠  " +
              str(type(self)) +
              " \nCREATED" + bcolors.ENDC + bcolors.ENDC)
        pass


class KrogothGantryMasterViewControllerSerializer(AbstractKrogothSerializer):

    class Meta:
        model = KrogothGantryMasterViewController
        fields = '__all__'

    def create(self, validated_data):
        print(bcolors.BOLD + bcolors.purple + "  🛠  " +
              str(type(self)) +
              " \nCREATED" + bcolors.ENDC + bcolors.ENDC)
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        uncommitedChange = UncommitedSQL.objects.create(name=validated_data['name'],
                                                        edited_by=jawn_user,
                                                        krogoth_class="KrogothGantryMasterViewController")
        return KrogothGantryMasterViewController.objects.create(**validated_data)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



class KrogothGantrySlaveViewControllerSerializer(AbstractKrogothSerializer):
    class Meta:
        model = KrogothGantrySlaveViewController
        fields = '__all__'

    def create(self, validated_data):
        print(bcolors.BOLD + bcolors.purple + "  🛠  " +
              str(type(self)) +
              " \nCREATED" + bcolors.ENDC + bcolors.ENDC)
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        uncommitedChange = UncommitedSQL.objects.create(name=validated_data['name'],
                                                        edited_by=jawn_user,
                                                        krogoth_class="KrogothGantrySlaveViewController")
        return KrogothGantrySlaveViewController.objects.create(**validated_data)


class KrogothGantryCategorySerializer(AbstractKrogothSerializer):

    class Meta:

        model = KrogothGantryCategory
        fields = ('id', 'name', 'title', 'weight', 'parent',)

    def update(self, instance, validated_data):
        is_subcat = True
        old_references = AKGantryMasterViewController.objects.none()
        filter_refs = ""
        replacement_path_part = ""
        old_name = instance.name
        if instance.parent is None:
            is_subcat = False
        if is_subcat:
            filter_refs = "krogoth_gantry/DVCManager/" + instance.parent.name + "/" + instance.name
            old_references = AKGantryMasterViewController.objects.filter(path_to_static__icontains=filter_refs)

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
            if is_subcat:
                if str(key) == 'name':
                    replacement_path_part = "krogoth_gantry/DVCManager/" + instance.parent.name + "/" + validated_data[
                        'name']
                    dvc_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
                    old = dvc_path + instance.parent.name + "/" + old_name
                    new = dvc_path + instance.parent.name + "/" + validated_data['name']
                    MoveToNewDirectory(old_path=old, new_path=new)

        for app in old_references:
            old = app.path_to_static
            app.path_to_static = old.replace(filter_refs, replacement_path_part)
            app.save()

        instance.save()
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        uncommitedChange = UncommitedSQL.objects.create(name=instance.name,
                                                        edited_by=jawn_user,
                                                        krogoth_class="KrogothGantryMasterViewController")
        return instance


class KrogothGantryDirectiveSerializer(AbstractKrogothSerializer):
    class Meta:
        model = KrogothGantryDirective
        fields = '__all__'

    def create(self, validated_data):
        print(bcolors.BOLD + bcolors.purple + "  🛠  " +
              str(type(self)) +
              " \nCREATED" + bcolors.ENDC + bcolors.ENDC)
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        uncommitedChange = UncommitedSQL.objects.create(name=validated_data['name'],
                                                        edited_by=jawn_user,
                                                        krogoth_class="KrogothGantryDirective")
        return KrogothGantryDirective.objects.create(**validated_data)


class KrogothGantryServiceSerializer(AbstractKrogothSerializer):
    class Meta:
        model = KrogothGantryService
        fields = '__all__'

    def create(self, validated_data):
        print(bcolors.BOLD + bcolors.purple + "  🛠  " +
              str(type(self)) +
              " \nCREATED" + bcolors.ENDC + bcolors.ENDC)
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        uncommitedChange = UncommitedSQL.objects.create(name=validated_data['name'],
                                                        edited_by=jawn_user,
                                                        krogoth_class="KrogothGantryService")
        return KrogothGantryService.objects.create(**validated_data)
