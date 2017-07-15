from django.shortcuts import render
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core import serializers
import json



class UnitFBIFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        all_units = UnitFbiData.objects.all()
        serialized_obj = serializers.serialize("json", all_units)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)


class WeaponTDFFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        all_objs = WeaponTDF.objects.all()
        serialized_obj = serializers.serialize("json", all_objs)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)


class DownloadTDFFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        all_objs = DownloadTDF.objects.all()
        serialized_obj = serializers.serialize("json", all_objs)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)


class FeatureTDFFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        all_objs = FeatureTDF.objects.all()
        serialized_obj = serializers.serialize("json", all_objs)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)
