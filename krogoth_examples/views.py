
# VIEW
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from krogoth_examples.models import Fruit, TextLabel, Manufacturer, Car, Topping, Pizza, Hotel, Occupant, \
    BasicImageUpload, BasicFileUpload
from krogoth_examples.serializers import FruitSerializer, TextLabelSerializer, ManufacturerSerializer, CarSerializer, \
    ToppingSerializer, PizzaSerializer, HotelSerializer, OccupantSerializer, BasicImageUploadSerializer, \
    BasicFileUploadSerializer



class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = (AllowAny,)

class TextLabelViewSet(viewsets.ModelViewSet):
    queryset = TextLabel.objects.all()
    serializer_class = TextLabelSerializer
    permission_classes = (AllowAny,)

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (AllowAny,)
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    permission_classes = (AllowAny,)
class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (AllowAny,)

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (AllowAny,)
class OccupantViewSet(viewsets.ModelViewSet):
    queryset = Occupant.objects.all()
    serializer_class = OccupantSerializer
    permission_classes = (AllowAny,)

class BasicImageUploadViewSet(viewsets.ModelViewSet):
    queryset = BasicImageUpload.objects.all()
    serializer_class = BasicImageUploadSerializer
    permission_classes = (AllowAny,)

class BasicFileUploadViewSet(viewsets.ModelViewSet):
    queryset = BasicFileUpload.objects.all()
    serializer_class = BasicFileUploadSerializer
    permission_classes = (AllowAny,)

