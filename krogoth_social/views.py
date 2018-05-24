from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_social.models import AKThread, AKThreadCategory, AKThreadSocialMedia
from krogoth_social.serializers import AKThreadCategorySerializer, AKThreadSerializer, AKThreadSocialMediaSerializer




class AKThreadCategoryViewSet(viewsets.ModelViewSet):
    queryset = AKThreadCategory.objects.all()
    serializer_class = AKThreadCategorySerializer
    permission_classes = (AllowAny,)


class AKThreadViewSet(viewsets.ModelViewSet):
    queryset = AKThread.objects.all()
    serializer_class = AKThreadSerializer
    permission_classes = (AllowAny,)


class AKThreadSocialMediaViewSet(viewsets.ModelViewSet):
    queryset = AKThreadSocialMedia.objects.all()
    serializer_class = AKThreadSocialMediaSerializer
    permission_classes = (AllowAny,)
