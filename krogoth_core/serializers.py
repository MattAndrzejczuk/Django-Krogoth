from rest_framework import serializers
from krogoth_core.models import AKFoundationAbstract


class AKFoundationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AKFoundationAbstract
        fields = '__all__'

