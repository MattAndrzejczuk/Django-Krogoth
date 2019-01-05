from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from colors import ink
from moho_extractor.models import GenericKGData
import json


PARAM_na = "uid"
PARAM_he = "header"
PARAM_co = "contents"
PARAM_c1 = "category_one"
PARAM_c2 = "category_two"


# from moho_extractor.generic_data_views import KGDataSerializer
class KGDataSerializer():

    def __init__(self, *args, **kwargs):
        super(KGDataSerializer, self).__init__(*args, **kwargs)

    @classmethod
    def toDict(cls, kgd):
        d = {}
        d[PARAM_na] = kgd.uid
        d[PARAM_he] = kgd.header
        d[PARAM_co] = kgd.contents
        d[PARAM_c1] = kgd.category_one
        d[PARAM_c2] = kgd.category_two
        return d
    @classmethod
    def toJson(cls, kgd):
        d = cls.toDict(kgd)
        return json.dumps(d, indent=2)
    @classmethod
    def toArray(cls, l):
        rr = []
        for i in l:
            rr.append(cls.toDict(i))
        return rr
    @classmethod
    def toJsonArray(cls, l):
        nl = cls.toArray(l)
        return json.dumps(nl, indent=2)


class GenericKGData_GetOneOrCreate(APIView):
    #authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)

    def get(self, request, format=None):
        ink.ppink('APIView : ')
        ink.pblue('AllDataMVC')
        if PARAM_na in request.GET:
            token = str(request.GET[PARAM_na])
            kg = GenericKGData.objects.filter(uid=token)
            if len(kg) == 0:
                return JsonResponse([], status=404, safe=False)
            else:
                return JsonResponse(KGDataSerializer.toJson(kg.first()), status=200, safe=False)

        else:
            err = {"results": "Missing GET parameter: '" + PARAM_c1 + "'"}
            return JsonResponse(err, status=405, safe=False)

    def post(self, request, format=None):
        if PARAM_na not in request.data:
            err = {"results": "Missing GET parameter: '" + PARAM_na + "'"}
            return JsonResponse(err, status=405, safe=False)
        if PARAM_he not in request.data:
            err = {"results": "Missing GET parameter: '" + PARAM_he + "'"}
            return JsonResponse(err, status=405, safe=False)
        if PARAM_co not in request.data:
            err = {"results": "Missing GET parameter: '" + PARAM_co + "'"}
            return JsonResponse(err, status=405, safe=False)

        uid = str(request.data[PARAM_na])
        header = str(request.data[PARAM_he])
        contents = str(request.data[PARAM_co])
        duplicate_check = GenericKGData.objects.filter(uid=uid)
        if len(duplicate_check) > 0:
            duplicate_check.first().delete()
        kgd = GenericKGData(uid=uid, header=header, contents=contents)
        if PARAM_c1 in request.data:
            kgd.category_one = request.data[PARAM_c1]
        if PARAM_c2 in request.data:
            kgd.category_two = request.data[PARAM_c2]
        kgd.save()
        return JsonResponse(KGDataSerializer.toJson(kgd), status=201, safe=False)


class GenericKGData_GetFromCategoryOne(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)
    def get(self, request, format=None):
        ink.ppink('APIView : ')
        ink.pblue('AllDataMVC')
        if PARAM_c1 in request.GET:
            token = str(request.GET[PARAM_c1])
            l = GenericKGData.objects.filter(category_one=token)
            js = KGDataSerializer.toJsonArray(l)
            return JsonResponse(js, status=200, safe=False)
        else:
            err = {"results": "Missing GET parameter: '"+PARAM_c1+"'"}
            return JsonResponse(err, status=405, safe=False)
