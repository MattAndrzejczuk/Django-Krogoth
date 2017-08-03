from django.shortcuts import render

from CommunityForum.serializers import ForumCategorySerializer, ForumPostSerializer, ForumReplySerializer
from CommunityForum.models import ForumCategory, ForumPost, ForumReply
# Create your views here.





class ForumCategoryViewset(viewsets.ModelViewSet):
    serializer_class = ForumCategorySerializer
    queryset = ForumCategory.objects.all()


class ForumPostViewset(viewsets.ModelViewSet):
    serializer_class = ForumPostSerializer
    queryset = ForumPost.objects.all()


class ForumReplyViewset(viewsets.ModelViewSet):
    serializer_class = ForumReplySerializer
    queryset = ForumReply.objects.all()


