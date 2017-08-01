from django.shortcuts import render
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core import serializers
import json



from LazarusDatabase.serializers import TotalAnnihilationModSerializer
from LazarusDatabase.models import TotalAnnihilationMod
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework import viewsets


from rest_auth.models import LazarusCommanderAccount


class TotalAnnihilationModViewset(viewsets.ModelViewSet):
    serializer_class = TotalAnnihilationModSerializer
    queryset = TotalAnnihilationMod.objects.all()



class CommanderAccountView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        all_units = LazarusCommanderAccount.objects.all()
        serialized_obj = serializers.serialize("json", all_units)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)

    def post(self, request, *args, **kwargs):
        faction = request.POST['faction']
        new_commander = LazarusCommanderAccount()
        new_commander.user = request.user
        new_commander.about_me = request.user
        new_commander.profile_pic = request.user
        new_commander.faction = faction

        new_commander.save()

        return Response('Welcome commander.')




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
        try:
            all_objs = DownloadTDF.objects.all()
            serialized_obj = serializers.serialize("json", all_objs)
            json_dict = json.loads(serialized_obj)
            list_response = []
            for item in json_dict:
                betterJson = item['fields']
                list_response.append(betterJson)
        except:
            return Response('Failed to find a parent unit for this TDF.')
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




#
#
# from django.shortcuts import render
# from dynamic_lazarus_page.models import AngularFuseApplication, NgIncludedHtml
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.core import serializers
# import json
#
#
# all_apps = AngularFuseApplication.objects.all()
# serialized_obj = serializers.serialize("json", all_apps)
# json_dict = json.loads(serialized_obj)
# list_all_apps = []
#
#
#
#
# for item in all_apps:
#     print(item.name)
#     print('\n\n\n')
#     print(item.js_controller)
#     print('\n\n\n')
#
#
# all_ng_included_html = NgIncludedHtml.objects.all()
# for item in all_ng_included_html:
#     print(item.name)
#     print('\n\n\n')
#     print(item.contents)
#     print('\n\n\n')


