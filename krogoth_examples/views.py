from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from krogoth_examples.models import Fruit
from krogoth_examples.serializers import FruitSerializer



# Create your views here.
class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = (AllowAny,)



