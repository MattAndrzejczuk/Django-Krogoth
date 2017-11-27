from rest_framework import serializers, exceptions
from chat.models import JawnUser
from LazarusV.models import *
#    V  -  5


class ModProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModProject
        fields = ('id', )
        
class ModPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModPublication
        fields = ('id', )

class ModBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModBuild
        fields = ('id', )

class WargamePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WargamePackage
        fields = ('id', )

class WargameFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WargameFile
        fields = ('id', )

class WargameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WargameData
        fields = ('id', )

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = ('id', )

class RatingCavedogBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingCavedogBase
        fields = ('id', )

class RatingModPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingModPublication
        fields = ('id', )