from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from krogoth_gantry.models.gantry_models import KrogothGantrySlaveViewController, KrogothGantryMasterViewController
from krogoth_gantry.krogoth_compiler import master_compiler


class DynamicJavaScriptInjector(APIView):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        name = request.GET['name']

        if 'lazy' in request.GET:
            lazy_token = request.GET['lazy']
            raw_js = master_compiler(username=request.user.username)
            js_response = raw_js.compiled_raw(named=[name, lazy_token]).replace("_LAZY_TOKEN_", lazy_token)
        else:
            raw_js = master_compiler(username=request.user.username)
            js_response = raw_js.compiled_raw(named=name)
        return HttpResponse(js_response, content_type='application/javascript; charset=utf-8')


class DynamicHTMLInjector(APIView):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        name = request.GET['name']
        application = KrogothGantryMasterViewController.objects.get(name=name)

        raw_html_response = application.view_html
        raw_html_response += '<style>' + application.style_css + application.get_theme_style + '</style>'

        if raw_html_response == '':
            raw_html_response += '<div layout="column" layout-padding layout-margin>'
            raw_html_response += '<h1>' + application.name.replace('_', ' ') + '</h1>'
            raw_html_response += '<h3>No Fuse App HTML Component</h3>'
            info = "You're seeing this message because no Fuse App HTML component with the type: HTML has not been " + \
                   "added to this Angular Fuse Application named " + application.name
            raw_html_response += "<p>" + info + "</p>"
            raw_html_response += '</div>'
        return HttpResponse(raw_html_response, content_type='text/html; charset=utf-8')


class DynamicHTMLSlaveInjector(APIView):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        name = request.GET['name']
        application = KrogothGantrySlaveViewController.objects.get(name=name)
        raw_html_response = application.view_html
        master = application.owner.get()
        raw_html_response += '<style>' + master.style_css + master.get_theme_style + '</style>'
        if raw_html_response == '':
            raw_html_response += '<div layout="column" layout-padding layout-margin>'
            raw_html_response += '<h1>' + application.name.replace('_', ' ') + '</h1>'
            raw_html_response += '<h3>No Fuse App HTML Component</h3>'
            info = "You're seeing this message because no Fuse App HTML component with the type: HTML has not been " + \
                   "added to this Angular Fuse Application named " + application.name
            raw_html_response += "<p>" + info + "</p>"
            raw_html_response += '</div>'
        return HttpResponse(raw_html_response, content_type='text/html; charset=utf-8')

