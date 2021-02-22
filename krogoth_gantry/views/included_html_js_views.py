from django.http import HttpResponse
import os
from rest_framework.views import APIView
from krogoth_gantry.functions.edit_core import IncludedHtmlMasterSerializer, IncludedJsMasterSerializer, \
    IncludedHtmlCoreTemplateSerializer
import json
from krogoth_gantry.models.moho_extractor_models import NgIncludedHtml, IncludedHtmlMaster, IncludedJsMaster, IncludedHtmlCoreTemplate
from krogoth_gantry.models.gantry_models import KrogothGantryMasterViewController

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAdminUser
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


class IncludedHtmlMasterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = IncludedHtmlMaster.objects.all().order_by('name')
    serializer_class = IncludedHtmlMasterSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('master_vc__name', )


class IncludedJsMasterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = IncludedJsMaster.objects.all().order_by('name')
    serializer_class = IncludedJsMasterSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('master_vc__name',)


class IncludedHtmlCoreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = IncludedHtmlCoreTemplate.objects.all().order_by('name')
    serializer_class = IncludedHtmlCoreTemplateSerializer

from krogoth_gantry.krogoth_modelview_pods import kg_publicstatic_text
from krogoth_gantry.models import DataServerEvents
import inspect


class NgIncludedHtmlView(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
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

            try:
                ksi = kg_publicstatic_text.objects.get(name=name)
                DataServerEvents.warn("NgIncludedHtml has been deprecated",
                                      inspect.getframeinfo(inspect.stack()[1][0]))
                return HttpResponse(ksi.contents)
            except:

                DataServerEvents.error("NgIncludedHtml has no KSI 'kg_publicstatic_text' for " + name,
                                       inspect.getframeinfo(inspect.stack()[1][0]))
                error += str(e) + " \n"
                html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + \
                       name + \
                       " TRACE: krogoth_gantry/views/middleware/included_html_js_views.py" + \
                       '</b> </p> </div>'
                html += '<script>alert("fatal krogoth_gantry error, unable to load HTML view: ' + name + \
                        ' due to: ' + error + '");</script>'
                html += '<h2>' + error + '</h2>'
            return HttpResponse(html)



from krogoth_gantry.models.core_models import AKFoundationAbstract


class KrogothFoundationView(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        unique_name = str(request.GET['unique_name'])
        js = AKFoundationAbstract.objects.get(unique_name=unique_name)
        ct = 'application/javascript'
        body = js.code.replace("var vm = this",
                               "console.log('DEPENDENCY CALLED: "+ unique_name +"');var vm = this")
        if unique_name == 'indexmodule':
            all_djangular = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
            my_apps = ''
            for application in all_djangular:
                my_apps += ("\t\t\t'app." + application.name + "',\n")
            body = js.code.replace('/*|#apps#|*/', my_apps)
        return HttpResponse(content_type=ct, content=body)


import base64
from jawn.settings import BASE_DIR


class LoadFileAsBase64View(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request):
        name = request.GET['name']

        path = BASE_DIR + '/static/styles/fancy_bgs/' + name
        if os.path.isfile(path) == True:
            with open(path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                return HttpResponse(content_type='text/plain', content=encoded_string)
        else:
            msg = "FAILED TO LOAD FILE AT PATH: " + path
            return HttpResponse(content_type='text/plain', content=msg)





