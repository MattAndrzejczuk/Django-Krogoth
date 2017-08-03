from django.shortcuts import render
from CommunityForum.models import ForumCategory, ForumPost, ForumReply
# Create your views here.





class ForumCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModDependency
        fields = '__all__'


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModDependency
        fields = '__all__'


class ForumReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModDependency
        fields = '__all__'


