from django.contrib.auth import login, logout
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from django.template import loader
from django.http import HttpResponse
import json
import os
from os import walk
from PIL import Image
from django.contrib.auth.models import User
from Djangular.models import DjangularMasterViewController, DjangularCategory, DjangularIcon
from GeneralWebsiteInfo.models import BootScreenLoader
from rest_framework.permissions import IsAuthenticated, AllowAny
from DatabaseSandbox.models import VisitorLogSB
from Djangular.models import DjangularService, DjangularDirective, DjangularSlaveViewController, \
    DjangularIcon, DjangularCategory, DjangularMasterViewController, SampleModelOne
from rest_framework import status
from rest_framework import viewsets
from Djangular.serializers import SampleModelOneSerializer
import subprocess


class MasterViewControllerEditorListView(APIView):
    def get(self, request, format=None):
        query = DjangularMasterViewController.objects.all()
        list = []

        print('\n\nGET - MasterViewControllerEditorListView \n\n')

        for mvc in query:
            obj = {}
            obj['id'] = mvc.id
            obj['name'] = mvc.name
            obj['title'] = mvc.title
            list.append(obj)

        return Response(list)

class MasterViewControllerEditorDetailView(APIView):
    def get(self, request, format=None):
        query = DjangularMasterViewController.objects.get(id=int(request.GET['id']))
        jsonobj = {}
        jsonobj['id'] = query.id
        jsonobj['name'] = query.name
        jsonobj['title'] = query.title
        jsonobj['view_html'] = query.view_html
        jsonobj['module_js'] = query.module_js
        jsonobj['controller_js'] = query.controller_js
        return Response(jsonobj)

    def put(self, request, *args, **kwargs):
        query = DjangularMasterViewController.objects.get(id=int(request.GET['id']))
        query.name = request.data['name']
        query.title = request.data['title']
        query.controller_js = request.data['controller_js']
        query.module_js = request.data['module_js']
        query.view_html = request.data['view_html']
        query.save()
        jsonobj = {}
        jsonobj['id'] = query.id
        jsonobj['name'] = query.name
        jsonobj['title'] = query.title
        jsonobj['view_html'] = query.view_html
        jsonobj['module_js'] = query.module_js
        jsonobj['controller_js'] = query.controller_js
        return Response(jsonobj)



class SlaveViewControllerEditorListView(APIView):
    def get(self, request, format=None):
        query = DjangularMasterViewController.objects.get(id=int(request.GET['master_id'])).djangular_slave_vc.all()
        list = []
        for svc in query:
            obj = {}
            obj['id'] = svc.id
            obj['name'] = svc.name
            obj['title'] = svc.title
            list.append(obj)
        return Response(list)

class SlaveViewControllerEditorDetailView(APIView):
    def get(self, request, format=None):
        query = DjangularSlaveViewController.objects.get(id=int(request.GET['id']))
        jsonobj = {}
        jsonobj['id'] = query.id
        jsonobj['name'] = query.name
        jsonobj['title'] = query.title
        jsonobj['view_html'] = query.view_html
        # jsonobj['module_js'] = query.module_js
        jsonobj['controller_js'] = query.controller_js
        return Response(jsonobj)

    def put(self, request, *args, **kwargs):
        query = DjangularSlaveViewController.objects.get(id=int(request.GET['id']))
        query.name = request.data['name']
        query.title = request.data['title']
        query.controller_js = request.data['controller_js']
        # query.module_js = request.data['module_js']
        query.view_html = request.data['view_html']
        query.save()
        jsonobj = {}
        jsonobj['id'] = query.id
        jsonobj['name'] = query.name
        jsonobj['title'] = query.title
        jsonobj['view_html'] = query.view_html
        # jsonobj['module_js'] = query.module_js
        jsonobj['controller_js'] = query.controller_js
        return Response(jsonobj)