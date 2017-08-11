from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
import json


# from CommunityForum.serializers import ForumCategorySerializer, ForumPostSerializer, ForumReplySerializer
from CommunityForum.models import ForumCategory, ForumPost, ForumReply
# Create your views here.

from django.views.decorators.csrf import csrf_exempt



# class ForumCategoryViewset(viewsets.ModelViewSet):
#     serializer_class = ForumCategorySerializer
#     queryset = ForumCategory.objects.all()
#
# class ForumPostViewset(viewsets.ModelViewSet):
#     serializer_class = ForumPostSerializer
#     queryset = ForumPost.objects.all()
#
# class ForumReplyViewset(viewsets.ModelViewSet):
#     serializer_class = ForumReplySerializer
#     queryset = ForumReply.objects.all()





class ForumCategoryMakeDefaults(APIView):
    def get(self, request, format=None):
        cat1 = ForumCategory(title='General')
        cat2 = ForumCategory(title='Bug Reports')
        cat3 = ForumCategory(title='Help & Tutorials')
        cat1.save()
        cat2.save()
        cat3.save()
        return Response('it worked!')

class ForumCategoryListView(APIView):
    def get(self, request, format=None):
        cats = ForumCategory.objects.filter(is_deleted=False)
        response_list = []
        for cat in cats:
            cat_json = {}
            cat_json['id'] = cat.id
            cat_json['title'] = cat.title
            response_list.append(cat_json)
        return Response(response_list)

class ForumCategoryDetailView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        cat_id = request.GET['cat_id']
        cat = ForumCategory.objects.get(id=int(cat_id))
        response_dict = {}
        response_dict['id'] = cat.id
        response_dict['title'] = cat.title
        response_dict['posts'] = []
        posts = ForumPost.objects.filter(category=cat)
        for post in posts:
            post_json = {}
            post_json['id'] = post.id
            post_json['title'] = post.title
            post_json['body'] = post.body
            post_json['author'] = {'username': post.author.username, 'id': post.author.id}
            post_json['pub_date'] = post.pub_date
            post_json['category'] = cat.id
            response_dict['posts'].append(post_json)

        return Response(response_dict)

class ForumPostDetailView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        post_id = request.GET['post_id']
        post = ForumPost.objects.get(id=post_id)
        replies = ForumReply.objects.filter(post=post.id)
        post_json = {}
        post_json['id'] = post.id
        post_json['title'] = post.title
        post_json['body'] = post.body
        post_json['author'] = {'username': post.author.username, 'id': post.author.id}
        post_json['pub_date'] = post.pub_date
        post_json['replies'] = []
        for reply in replies:
            reply_json = {}
            reply_json['id'] = reply.id
            reply_json['author'] = {'username': reply.author.username, 'id': reply.author.id}
            reply_json['body'] = reply.body
            reply_json['pub_date'] = reply.pub_date
            post_json['replies'].append(reply_json)
        return Response(post_json)

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        try:
            newpost_title = request.data['title']
            newpost_body = request.data['body']
            newpost_category = request.data['category']
            newpost_author = request.user
            newpost = ForumPost()
            newpost.title = newpost_title
            newpost.author = newpost_author
            newpost.body = newpost_body
            cat = ForumCategory.objects.get(id=int(newpost_category))
            newpost.category = cat
            newpost.save()

            responsePost = {}
            responsePost['id'] = newpost.id
            responsePost['title'] = newpost.title
            responsePost['success'] = "New thread created."

            return Response(
                responsePost,
                status=201
            )

        except:
            return Response(
                {"failed": "New thread failed to create."},
                status=405
            )


class ForumReplySubmitView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        return Response(
            {"warning": "You don't belong here."},
            status=405
        )

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data


        try:
            newreply_author = request.user
            newreply_body = request.data['body']
            newreply_post = request.data['post']
            post = ForumPost.objects.get(id=int(newreply_post))

            reply = ForumReply()
            reply.author = newreply_author
            reply.body = newreply_body
            reply.post = post

            reply.save()
            return Response(
                {"success": "New reply created."},
                status=201
            )

        except:
            return Response(
                {"failed": "New thread failed to create."},
                status=405
            )