from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_3rdparty_api.models import BaseCallbackEndpoint
import json
from urllib.request import urlopen

# Create your views here.

class GenericCallbackURIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        params = request.query_params
        record_of_this = BaseCallbackEndpoint(full_uri=request.build_absolute_uri(), uri_request_params=params)
        record_of_this.save()
        css = "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'/>"
        json_dump = json.dumps(params, indent=2, sort_keys=True)
        print(json_dump)
        htmlText = "<br/><p>URI:</p><p>" + request.build_absolute_uri() + "</p><br/><textarea>" + json_dump + \
                   "</textarea>"
        return HttpResponse(css + '<h1>API Callback</h1>' + htmlText)


def get_json_from_dogs_ceo(url: str) -> str:
    webURL = urlopen(url)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    obj = json.loads(data.decode(encoding))
    return obj
# - - - - - - - DOG API - - - - - - - -
# https://dog.ceo/api/breeds/list/all/
class RESTfulProxy_AllDogs(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        dogsrest = 'https://dog.ceo/api/breeds/list/all'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)


# https://dog.ceo/api/breeds/image/random/
class RESTfulProxy_RandomDogImage(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        dogsrest = 'https://dog.ceo/api/breeds/image/random'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)


# https://dog.ceo/api/breeds/list/
class RESTfulProxy_AllBreeds(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        dogsrest = 'https://dog.ceo/api/breeds/list'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)


# https://dog.ceo/api/breed/mastiff/images/
class RESTfulProxy_ListImagesForBreed(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        dogsrest = 'https://dog.ceo/api/breed/mastiff/images'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)


# https://dog.ceo/api/breed/mastiff/images/random/
class RESTfulProxy_GetRandonImageForBreed(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        breed = request.GET['breed']
        dogsrest = 'https://dog.ceo/api/breed/' + breed + '/images/random'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)


# https://dog.ceo/api/breed/mastiff/list/
class RESTfulProxy_GetListOfSubBreedsUsingBreed(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        dogsrest = 'https://dog.ceo/api/breed/mastiff/list'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)


# https://dog.ceo/api/breed/mastiff/bull/images/
class RESTfulProxy_ListImagesForSpecificBreedAndSubBreed(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        dogsrest = 'https://dog.ceo/api/breed/mastiff/bull/images'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)


# https://dog.ceo/api/breed/mastiff/bull/images/random/
class RESTfulProxy_GetImageForSpecificBreedAndSubBreed(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        dogsrest = 'https://dog.ceo/api/breed/mastiff/bull/images/random'
        js = get_json_from_dogs_ceo(url=dogsrest)
        return JsonResponse(js)
# - - - - - - - /DOG API - - - - - - -
