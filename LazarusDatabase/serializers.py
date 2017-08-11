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

        try:
            SelectedAssetUploadRepository.objects.filter(jawn_user=jawn_user)

        except:
            c = SelectedAssetUploadRepository.objects.create(name=validated_data['name'],
                                                             description=validated_data['description'],
                                                             author=jawn_user)

            ### SEND MESSAGE TO REDIS PUB AFTER CREATING THIS OBJECT
            # j = SelectedAssetUploadRepositorySerializer(c, context=self.context)
            # json = JSONRenderer().render(j.data)
            # message = RedisMessage(json.decode("utf-8"))
            # RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
            return c

    def update(self, instance, validated_data):
        for key in validated_data.keys():

            ## if is_selected is set to true, set all other repos to false:
            if key == 'is_selected':
                if validated_data[key] == True:
                    allRepos = SelectedAssetUploadRepository.objects.all()
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
        fields = '__all__'


class LazarusModProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModProject
        fields = '__all__'


class LazarusModAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModAsset
        fields = '__all__'


class LazarusModDependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModDependency
        fields = '__all__'


