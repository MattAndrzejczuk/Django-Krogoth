from rest_framework import serializers, exceptions
from LazarusV import models
#    V  -  5



class ModProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModProject
        fields = ('author', 'name', 'is_public', 'date_created', 'date_modified')

class ModPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModPublication
        fields = ('title', 'description', 'requirements', 'support', 'is_private',
                  'website_url', 'total_minor_milestones', 'total_major_milestones', 'kind')

class ModBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModBuild
        fields = ('rated_by', 'v_major', 'v_minor', 'download_url', 'build_date', )

class CavedogBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CavedogBase
        fields = ('keyname', 'snowflake', 'thumbnail_url', 'raw_tdf', 'data_dict', 'date_created', )

class WargamePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WargamePackage
        fields = ('parent_proj', 'name', 'thumbnail_url', )

class WargameFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WargameFile
        fields = ('pack', 'path', 'unique_name', 'kind', 'thumbnail_url', )

class WargameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WargameData
        fields = ('pack', 'source', 'unique_name', 'kind', 'thumbnail_url', )

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRating
        fields = ('rated_by', 'total_votes', 'date_rated', )

class RatingCavedogBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RatingCavedogBase
        fields = ('cavedog_base_tdf', 'vote_value', )

class RatingModPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RatingModPublication
        fields = ('lazarus_published_mod', 'vote_value', )