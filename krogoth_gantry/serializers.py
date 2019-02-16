from rest_framework import serializers
from rest_framework import viewsets, serializers, generics, filters
from krogoth_admin.models import UncommitedSQL
from krogoth_gantry.models import KrogothGantrySlaveViewController, \
    KrogothGantryIcon, KrogothGantryCategory, KrogothGantryMasterViewController, KrogothGantryDirective, \
    KrogothGantryService, AKGantryMasterViewController
from jawn.settings import BASE_DIR
from krogoth_chat.models import JawnUser
from krogoth_gantry.helpers.os_directory import MoveToNewDirectory
from krogoth_gantry.management.commands.installdjangular import bcolors

class KrogothGantryIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrogothGantryIcon
        fields = '__all__'


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
    icon = KrogothGantryIconSerializer(many=False, read_only=True)

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
    icon = KrogothGantryIconSerializer(read_only=True)

    class Meta:

        model = KrogothGantryCategory
        fields = ('id', 'name', 'title', 'weight', 'icon', 'parent',)

    def update(self, instance, validated_data):
        print("ID: " + str(instance.id))
        is_subcat = True
        old_references = AKGantryMasterViewController.objects.none()
        filter_refs = ""
        replacement_path_part = ""
        old_name = instance.name
        if instance.parent is None:
            is_subcat = False
        if is_subcat:
            print("parent: " + str(instance.parent.name))
            # krogoth_gantry/DVCManager/Web_Sockets/Advanced/Chat_App/
            filter_refs = "krogoth_gantry/DVCManager/" + instance.parent.name + "/" + instance.name
            old_references = AKGantryMasterViewController.objects.filter(path_to_static__icontains=filter_refs)
            print("\n\nDiscovered " + str(len(old_references)) + " MVCs that need an update made to their static path.")
            print("Their old path will be replaced: " + filter_refs)

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
            # print(bcolors.BOLD + bcolors.blue + "  🛠  " +
            #       str(type(self)) + " : " + str(key) +
            #       " \nUPDATED CATEGORY: " + bcolors.ENDC + bcolors.ENDC)
            if is_subcat:
                if str(key) == 'name':
                    replacement_path_part = "krogoth_gantry/DVCManager/" + instance.parent.name + "/" + validated_data[
                        'name']
                    print("With this new path substring   : " + replacement_path_part)
                    dvc_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
                    old = dvc_path + instance.parent.name + "/" + old_name
                    new = dvc_path + instance.parent.name + "/" + validated_data['name']
                    print("RENAMING DIRECTORY: ")
                    print("OLD: " + old)
                    print("NEW: " + new)
                    MoveToNewDirectory(old_path=old, new_path=new)

        for app in old_references:
            old = app.path_to_static
            print("Changing " + app.name + "'s path_to_static.")
            app.path_to_static = old.replace(filter_refs, replacement_path_part)
            app.save()
            print("It's new path is now: " + app.path_to_static)

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
