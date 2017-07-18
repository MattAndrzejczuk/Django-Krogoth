from Djangular.models import SampleModelOne
from rest_framework import serializers, exceptions





class SampleModelOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleModelOne
        fields = '__all__'


