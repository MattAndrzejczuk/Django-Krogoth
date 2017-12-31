from chat.models import JawnUser
from rest_framework import serializers

from krogoth_examples.models import Fruit



class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'
