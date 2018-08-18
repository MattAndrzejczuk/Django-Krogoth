from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_social.models import AKThread, AKThreadCategory, AKThreadSocialMedia
from krogoth_social.serializers import AKThreadCategorySerializer, AKThreadSerializer, AKThreadSocialMediaSerializer, AKThreadReplySocialMediaSerializer
from rest_framework.views import APIView
from datetime import datetime
from django.http import HttpResponse


class AKThreadCategoryViewSet(viewsets.ModelViewSet):
    queryset = AKThreadCategory.objects.all()
    serializer_class = AKThreadCategorySerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('uid',)
    


class AKThreadViewSet(viewsets.ModelViewSet):
     queryset = AKThread.objects.all()
     serializer_class = AKThreadSerializer
     permission_classes = (AllowAny,)
     filter_backends = (filters.DjangoFilterBackend,)
     filter_fields = ('author', 'parent', 'category',)

class AKThreadListView(generics.ListAPIView):
    queryset = AKThread.objects.all()
    serializer_class = AKThreadSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('date_modified', )
    ordering = ('date_modified',)


class AKThreadSocialMediaViewSet(viewsets.ModelViewSet):
    queryset = AKThreadSocialMedia.objects.filter(parent=None)
    serializer_class = AKThreadSocialMediaSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('author', 'parent', 'category',)

class AKThreadSocialMediaReplyViewSet(viewsets.ModelViewSet):
    queryset = AKThreadSocialMedia.objects.filter(title="REPLY")
    serializer_class = AKThreadReplySocialMediaSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('author', 'parent', 'category',)


class update_thread_moddate(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        thread = request.GET['threadId']         
        op = AKThread.objects.get(uid=thread)
        op.date_modified = datetime.now()
        op.save(update_fields=["date_modified"]) 
        return HttpResponse("ITS GOOD", content_type='text/html; charset=utf-8')