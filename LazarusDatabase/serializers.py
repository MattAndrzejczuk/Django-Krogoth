from LazarusDatabase.models import TotalAnnihilationMod, LazarusModProject, LazarusModAsset, \
    LazarusModDependency, SelectedAssetUploadRepository, HPIUpload, LazarusPublicAsset
from rest_framework import serializers, exceptions
from chat.models import JawnUser
from DatabaseSandbox.models import TotalAnnihilationUploadedFile

import subprocess
import os



class SelectedAssetUploadRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedAssetUploadRepository
        fields = ('id', 'name', 'description', 'created', 'author', 'is_selected')

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        SelectedAssetUploadRepository.objects.filter(author=jawn_user)
        c = SelectedAssetUploadRepository.objects.create(name=validated_data['name'],
                                                         is_selected=False,
                                                         description=validated_data['description'],
                                                         author=jawn_user)
        return c

    def update(self, instance, validated_data):
        for key in validated_data.keys():

            ## if is_selected is set to true, set all other repos to false:
            if key == 'is_selected':
                if validated_data[key] == True:
                    jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
                    allRepos = SelectedAssetUploadRepository.objects.filter(author=jawn_user)
                    for repo in allRepos:
                        if repo.name != instance.name:
                            repo.is_selected = False
                            repo.save()
            setattr(instance, key, validated_data[key])
        instance.save()

        a = SelectedAssetUploadRepositorySerializer(instance, context=self.context)

        return instance


class TotalAnnihilationModSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalAnnihilationMod
        fields = ('id', 'name', 'description', 'is_selected',)


class LazarusModProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModProject
        fields = ('id', 'name', 'description', 'is_selected', 'created_by', 'created',)

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        LazarusModProject.objects.filter(created_by=jawn_user)
        c = LazarusModProject.objects.create(name=validated_data['name'],
                                             is_selected=False,
                                             description=validated_data['description'],
                                             created_by=jawn_user)
        return c

    def update(self, instance, validated_data):
        for key in validated_data.keys():

            ## if is_selected is set to true, set all other repos to false:
            if key == 'is_selected':
                if validated_data[key] == True:
                    jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
                    allRepos = LazarusModProject.objects.filter(created_by=jawn_user)
                    for repo in allRepos:
                        if repo.name != instance.name:
                            repo.is_selected = False
                            repo.save()
            setattr(instance, key, validated_data[key])
        instance.save()

        a = SelectedAssetUploadRepositorySerializer(instance, context=self.context)

        return instance


class LazarusModAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModAsset
        fields = ('id', 'name', 'type', 'project_id', 'uploader')

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        LazarusModAsset.objects.filter(uploader=jawn_user)
        c = LazarusModAsset.objects.create(name=validated_data['name'],
                                           type=validated_data['type'],
                                           project_id=validated_data['project_id'],
                                           uploader=jawn_user)
        return c


class LazarusModDependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModDependency
        fields = '__all__'


class LazarusPublicAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusPublicAsset
        fields = ("id", "likes","dislikes","side","name","encoded_path","tags","description","unitpic","HP",
                  "size","energyCost","metalCost","is_deleted","is_featured","fbiSnowflake",)

    def update(self, instance, validated_data):
        instance.save()
        return instance




import threading




class HPIUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HPIUpload
        fields = ('upload', 'name', 'type', 'size',)


    def create(self, validated_data):


        def extract_hpi_in_other_thread(hpi):
            print('FILE UPLOADED: ')
            print('c.upload.name')
            print(hpi.upload.name)
            file_name = str(hpi.upload.name).replace('ta_data/', '')
            print("str(c.upload.name).replace('ta_data/', '')")
            print(str(hpi.upload.name).replace('ta_data/', ''))
            extraction_directory = '/usr/src/persistent/media/ta_data/' + file_name[:-4]
            print('extraction_directory')
            print(extraction_directory)
            os.system('mkdir ' + extraction_directory)
            ufo_path = '/usr/src/persistent/media/' + hpi.upload.name
            bash_cmd = ['sh', 'extractTA_Mod.sh', ufo_path, extraction_directory]
            run_extraction_bash = str(subprocess.check_output(bash_cmd))
            rename_files_bash = "bash bashRenameStuffToLowerInDirectory_public.sh " + file_name[:-4] + "/."
            os.system(rename_files_bash)
            print('executing bash: ')
            print(rename_files_bash)
            but_DB = TotalAnnihilationUploadedFile(file_name=file_name,
                                                   download_url=extraction_directory + '.ufo',
                                                   system_path=extraction_directory,
                                                   uploader=self.context['request'].user.username,
                                                   file_type=file_name[-3:],
                                                   HPI_Extractor_Log=run_extraction_bash
                                                   )
            currentUploadRepo = SelectedAssetUploadRepository.objects.filter(author=jawn_user)
            thisdesignation = currentUploadRepo[0].name + '_SelectedAssetUploadRepository'
            for repo in currentUploadRepo:
                if repo.is_selected == True:
                    thisdesignation = repo.name + '_SelectedAssetUploadRepository'
                    break
            thiscategory = hpi.id
            but_DB.designation = thisdesignation
            but_DB.hpi_upload_id = thiscategory
            but_DB.save()
            hpi.TA_uploaded_file_log = but_DB.id
            hpi.save()


        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        print(jawn_user)
        print('is uploading a file...')
        c = HPIUpload.objects.create(name=validated_data['name'],
                                     type=validated_data['type'],
                                     size=validated_data['size'],
                                     uploaded_by=jawn_user,
                                     upload=validated_data['upload'])
        extract_thread = threading.Thread(target=extract_hpi_in_other_thread, args=(c,))
        print('starting thread...')
        extract_thread.start()
        return c
























