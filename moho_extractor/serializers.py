from rest_framework import serializers
from moho_extractor.models import IncludedHtmlMaster


class IncludedHtmlMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncludedHtmlMaster
        fields = '__all__'

