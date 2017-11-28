from rest_framework import serializers, exceptions
from LazarusV import models
#    V  -  5



class ModProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModProject
        fields = ('id', )

class ModPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModPublication
        fields = ('id', )

class ModBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModBuild
        fields = ('id', )

class WargamePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WargamePackage
        fields = ('id', )

class WargameFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WargameFile
        fields = ('id', )

class WargameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WargameData
        fields = ('id', )

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRating
        fields = ('id', )

class RatingCavedogBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RatingCavedogBase
        fields = ('id', )

class RatingModPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RatingModPublication
        fields = ('id', )