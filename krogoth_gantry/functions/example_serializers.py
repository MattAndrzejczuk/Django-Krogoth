
# CONTROLLER
from rest_framework import serializers
from krogoth_gantry.models.example_models import Fruit, TextLabel, Manufacturer, Car, Topping, \
    Pizza, Hotel, Occupant, BasicImageUpload, BasicFileUpload



class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'

class TextLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextLabel
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
class OccupantSerializer(serializers.ModelSerializer):
    # location = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Occupant
        fields = '__all__'

class BasicImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicImageUpload
        fields = '__all__'

class BasicFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicFileUpload
        fields = '__all__'