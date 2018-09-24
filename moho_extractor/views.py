from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from moho_extractor.serializers import IncludedHtmlMasterSerializer, IncludedJsMasterSerializer, \
    IncludedHtmlCoreTemplateSerializer

from moho_extractor.models import NgIncludedHtml, IncludedHtmlMaster, IncludedJsMaster, IncludedHtmlCoreTemplate
from krogoth_gantry.models import KrogothGantryMasterViewController

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, filters
CCD = {
    0: '\033[0m',  # end

    200: '\033[3m',  # italic
    201: '\033[4m',  # underline
    202: '\033[1m',  # bold
    203: '\033[2m',  # darkish

    108: '\033[7m',  # highlight
    107: '\033[107m',  # oj highlight
    106: '\033[106m',  # cyan highlight
    105: '\033[105m',  # magenta highlight
    104: '\033[104m',  # blue highlight
    103: '\033[103m',  # yellow highlight
    102: '\033[102m',  # green highlight
    101: '\033[101m',  # red highlight
    100: '\033[100m',  # purple highlight

    1: '\033[31m',  # dark red
    2: '\033[32m',  # dark green
    3: '\033[33m',  # dark yellow
    4: '\033[34m',  # dark blue
    5: '\033[35m',  # dark magenta
    6: '\033[36m',  # dark cyan
    7: '\033[37m',  # dark yellow

    10: '\033[90m',  # bright purple
    11: '\033[30m',  # purple
    12: '\033[97m',  # oj
    13: '\033[96m',  # cyan
    14: '\033[95m',  # magenta
    15: '\033[94m',  # blue
    16: '\033[93m',  # yellow
    17: '\033[92m',  # green neon
    18: '\033[91m',  # red
}

from jawn.settings import DEBUG
def krogoth_debug(msg):
    if DEBUG == True:
        try:
            print(CCD[4] + '[MohoExtractor]' + CCD[0], end=CCD[10] + " >>> " + CCD[0])
            print(str(msg), end="\n")
        except:
            pass


class IncludedHtmlMasterViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IncludedHtmlMaster.objects.all().order_by('name')
    serializer_class = IncludedHtmlMasterSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('master_vc__name', )


class IncludedJsMasterViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IncludedJsMaster.objects.all().order_by('name')
    serializer_class = IncludedJsMasterSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('master_vc__name',)


class IncludedHtmlCoreViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IncludedHtmlCoreTemplate.objects.all().order_by('name')
    serializer_class = IncludedHtmlCoreTemplateSerializer







class NgIncludedHtmlView(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        krogoth_debug('\033[92m')
        krogoth_debug(request.GET)
        krogoth_debug('\033[0m')
        name = str(request.GET['name'])
        error = ""
        try:
            try:
                data = str(request.GET['data'])
                html_view = NgIncludedHtml.objects.get(name=name)
                final_html = html_view.contents.replace('INJECTED_DATA', data)
                return HttpResponse(final_html)
            except Exception as e:
                error += str(e) + " \n"
                html_view = NgIncludedHtml.objects.get(name=name)
                return HttpResponse(html_view.contents)
        except Exception as e:

            error += str(e) + " \n"
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            html += '<script>alert("fatal krogoth_gantry error, unable to load HTML view: ' + name + \
                    ' due to: ' + error + '");</script>'
            html += '<h2>' + error + '</h2>'
            return HttpResponse(html)



from krogoth_core.models import AKFoundationAbstract


class KrogothFoundationView(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        unique_name = str(request.GET['unique_name'])
        js = AKFoundationAbstract.objects.get(unique_name=unique_name)
        ct = 'application/javascript'
        body = js.code.replace("var vm = this",
                               "console.log('DEPENDENCY CALLED: "+ unique_name +"');var vm = this")

        krogoth_debug('\033[91m')
        try:
            if js.custom_key_values is not None:
                for key, value in js.custom_key_values.items():
                    p1 = 'krogoth_injected={};'
                    obj = {}
                    obj[key] = value
                    print(obj)
                    body = body.replace(p1,
                                        'krogoth_injected=' + json.dumps(obj) + ';')
            krogoth_debug('\033[0m')
        except:
            krogoth_debug('BOOM!')
        if unique_name == 'indexmodule':
            all_djangular = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
            my_apps = ''
            for application in all_djangular:
                my_apps += ("\t\t\t'app." + application.name + "',\n")
            body = js.code.replace('/*|#apps#|*/', my_apps)
        return HttpResponse(content_type=ct, content=body)


import os
import base64
from jawn.settings import BASE_DIR


class LoadFileAsBase64View(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request):
        name = request.GET['name']
        path = BASE_DIR + '/static/fancy_bgs/' + name
        # if os.path.isfile(path) == True:
        #     pass
        # else:
        #     raise IOError()
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return HttpResponse(content_type='text/plain', content=encoded_string)


import json

from urllib.request import urlopen

def get_json_from_dogs_ceo(url: str) -> str:
    krogoth_debug('\033[92m' + url + '\033[0m')
    webURL = urlopen(url)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    obj = json.loads(data.decode(encoding))
    krogoth_debug(json.dumps(obj, indent=2, sort_keys=True))
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