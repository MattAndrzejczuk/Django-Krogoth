
import os
from django.shortcuts import render

from krogoth_gantry.models import KrogothGantryMasterViewController
from krogoth_core.models import AKFoundationAbstract, AKBowerComponent

from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from krogoth_core.models import AKFoundationAbstract
from krogoth_core.serializers import AKFoundationSerializer

from django.template import loader
from django.http import HttpResponse
from jawn.settings import STATIC_KROGOTH_MODE, APP_VERSION


class AKFoundationViewSet(viewsets.ModelViewSet):
    queryset = AKFoundationAbstract.objects.all().order_by('last_name')
    serializer_class = AKFoundationSerializer
    permission_classes = (AllowAny, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('unique_name', 'first_name', 'last_name', 'ext', )


def index(request):
    permission_classes = (AllowAny,)
    template = loader.get_template('index.html')
    splash_title = 'Krogoth'
    font_size = 36
    splash_logo_bg_color = 'antiquewhite'
    width = 250
    main_bg_color = 'darkolive'
    font_color = 'black'

    KrogothGantryMasterViewControllers = []
    if STATIC_KROGOTH_MODE == False:
        all_applications = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
        for application in all_applications:
            KrogothGantryMasterViewControllers.append('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + application.name)
    else:
        all_applications = os.listdir('static/compiled')
        for application in all_applications:
            KrogothGantryMasterViewControllers.append('/static/compiled/' + application)
    version_build = 'Krogoth ' + APP_VERSION
    seo_title = "Krogoth "
    seo_description = 'description'
    seo_description += ', description - 2'
    KrogothMainComponents = []
    all_parts = AKFoundationAbstract.objects.filter(is_selected_theme=True)
    for p in all_parts:
        if p.first_name == "core" or \
                p.first_name == "index" or \
                p.first_name == "main" or \
                p.first_name == "quick-panel" or \
                p.first_name == "toolbar" or \
                p.first_name == "navigation":
            pass
        else:
            KrogothMainComponents.append(p.unique_name)
    all_bowers = AKBowerComponent.objects.all()
    context = {
        "version_build": version_build,
        "all_bowers": all_bowers,
        "core":KrogothMainComponents,
        "message": seo_title,
        "description": seo_description,
        "KrogothGantryMasterViewControllers": KrogothGantryMasterViewControllers,
        "splash_title": splash_title,
        "font_size": font_size,
        "splash_logo_bg_color": splash_logo_bg_color,
        "width": width,
        "main_bg_color": main_bg_color,
        "font_color": font_color
    }
    return HttpResponse(template.render(context, request))
