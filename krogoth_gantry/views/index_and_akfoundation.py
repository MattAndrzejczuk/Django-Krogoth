
import os

from krogoth_gantry.models import IncludedHtmlCoreTemplate
from krogoth_gantry.models.gantry_models import KrogothGantryMasterViewController
from krogoth_gantry.models.core_models import AKBowerComponent


from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from krogoth_gantry.models.core_models import AKFoundationAbstract
from krogoth_gantry.functions.akfoundation import AKFoundationSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from django.template import loader
from django.http import HttpResponse
from jawn.settings import STATIC_KROGOTH_MODE #, APP_VERSION
from django.template import Context, Template

# from krogoth_gantry.views.middleware.dj_tmpl_rendered import load_custom_css, load_krogoth_css, load_background_css, \
#     load_core_css, load_core_elements_css

from krogoth_gantry.models.krogoth_manager import KrogothVisitorTracking

class AKFoundationViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = AKFoundationAbstract.objects.all().order_by('last_name')
    serializer_class = AKFoundationSerializer
    permission_classes = (AllowAny, )
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('unique_name', 'first_name', 'last_name', 'ext', )


# * * * * *
# Any new global CSS customizations should be added here.
# Edit the CSS document at:
# static/web/core/html/layouts/CSS_CustomGlobals.html

def load_custom_css():
    css = IncludedHtmlCoreTemplate.objects.get(name="CSS_CustomGlobals.html")
    template = Template(css.contents)
    context = Context({"foo1": "bar1"})
    rendered = template.render(context)
    return rendered


# * * * * *
# non-Google CSS stylesheets:

def load_krogoth_css():
    css = IncludedHtmlCoreTemplate.objects.get(name="CSS_Krogoth.html")
    template = Template(css.contents)
    context = Context({"foo1": "bar1"})
    rendered = template.render(context)
    return rendered


def load_background_css():
    css = IncludedHtmlCoreTemplate.objects.get(name="CSS_Background.html")
    template = Template(css.contents)
    context = Context({"foo1": "bar1"})
    rendered = template.render(context)
    return rendered


# * * * * *
# core and core elements are the default AngularJS styles from Google:

def load_core_css():
    css = IncludedHtmlCoreTemplate.objects.get(name="CSS_Core.html")
    template = Template(css.contents)
    context = Context({"foo1": "bar1"})
    rendered = template.render(context)
    return rendered


def load_core_elements_css():
    css = IncludedHtmlCoreTemplate.objects.get(name="CSS_CoreElements.html")
    template = Template(css.contents)
    context = Context({"foo1": "bar1"})
    rendered = template.render(context)
    return rendered




def index(request):
    permission_classes = (AllowAny,)
    template = loader.get_template('index.html')
    splash_title = 'Krogoth'
    font_size = 36
    splash_logo_bg_color = 'antiquewhite'
    width = 250
    main_bg_color = 'darkolive'
    font_color = 'black'


    try:
        usr = 'ANONYMOUS'
        if request.user:
            usr = request.user.username
        count_this = KrogothVisitorTracking(remote_addr=request.META['REMOTE_ADDR'],
                                            remote_port=request.META['REMOTE_PORT'],
                                            http_user_agent=request.META['HTTP_USER_AGENT'],
                                            username=usr)
        count_this.save()
    except:
        print('\n\n\nFAILED TO TRACE\n\n\n')

    KrogothGantryMasterViewControllers = []
    if STATIC_KROGOTH_MODE == False:
        all_applications = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
        for application in all_applications:
            KrogothGantryMasterViewControllers.append('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + application.name)
    else:
        all_applications = os.listdir('static/compiled')
        for application in all_applications:
            KrogothGantryMasterViewControllers.append('/static/compiled/' + application)
    version_build = 'Krogoth v1.0.02'
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
        "font_color": font_color,
        "load_custom_css": load_custom_css(),
        "load_krogoth_css": load_krogoth_css(),
        "load_background_css": load_background_css(),
        "load_core_css": load_core_css(),
        "load_core_elements_css": load_core_elements_css(),
    }
    return HttpResponse(template.render(context, request))


