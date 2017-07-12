from django.shortcuts import render

from django.http import HttpResponse



# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from PhotoGalleryManager.models import GalleryCollection, GalleryItem






class ScaffoldView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        html = '<div> <h1>It works!!!</h1> <p> Nothing to see here </p> </div>'
        return HttpResponse(html)


class GalleryCollectionList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        collection_query = GalleryCollection.objects.all()
        response_list = []
        for item in collection_query:
            new_json = {}
            new_json['id'] = item.id
            new_json['unique_name'] = item.unique_name
            new_json['pub_date'] = item.pub_date
            new_json['title'] = item.title
            new_json['subheading'] = item.subheading
            new_json['description'] = item.description
            response_list.append(new_json)
        return Response(response_list)


class GalleryItemList(APIView):
    def get(self, request, format=None):
        collection_name = request.GET['collection_name']
        collection_query = GalleryCollection.objects.get(unique_name=collection_name)
        gallery_items = GalleryItem.objects.filter(parent_gallery=collection_query)
        response_list = []
        for item in gallery_items:
            new_json = {}
            new_json['pic_url'] = '/media/' + str(item.model_pic)
            new_json['title'] = item.title
            new_json['subheading'] = item.subheading
            new_json['pub_date'] = item.pub_date
            new_json['description'] = item.description
            new_json['id'] = item.id
            response_list.append(response_list)

        return Response(response_list)
# unique_name

class GalleryItemDetail(APIView):
    def get(self, request, format=None):
        item_id = request.GET['id']
        gallery_item = GalleryItem.objects.get(id=item_id)
        response_json = {}
        response_json['pic_url'] = '/media/' + gallery_item.model_pic
        response_json['title'] = gallery_item.title
        response_json['subheading'] = gallery_item.subheading
        response_json['pub_date'] = gallery_item.pub_date
        response_json['description'] = gallery_item.description
        response_json['id'] = gallery_item.id

        return Response(response_json)

