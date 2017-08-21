from LazarusDatabase.models import TotalAnnihilationMod, LazarusModProject, LazarusModAsset, \
    LazarusModDependency, SelectedAssetUploadRepository
from rest_framework import serializers, exceptions
from chat.models import JawnUser


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
        fields = ('id', 'name', 'type', 'project_id', 'author')

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
