from django.shortcuts import render
from GeneralWebsiteInfo.models import WebsiteColorTheme, WebsiteLayout, NavigationBar, BootScreenLoader


from rest_framework.permissions import IsAuthenticated, AllowAny


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



# GeneralWebsiteInfo

###   WebsiteColorThemeView
###   WebsiteLayoutView
###   NavigationBarView
###   BootScreenLoaderView




class WebsiteColorThemeView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])
        try:
            html_view = WebsiteColorTheme.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)

class WebsiteLayoutView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])

        try:
            html_view = WebsiteLayout.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)

class NavigationBarView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])

        try:
            html_view = NavigationBar.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)

class BootScreenLoaderView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])

        try:
            html_view = BootScreenLoader.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)