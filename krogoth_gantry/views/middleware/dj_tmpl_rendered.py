# Author - Matt Andrzejczuk

### aside from index.html, all HTML and JS loaded here takes
### advantage of the Django templating engine

from django.http import HttpResponse
from django.template import Context, Template
from krogoth_gantry.models.moho_extractor_models import IncludedHtmlCoreTemplate


def example_view(request):
    template = Template('My name is, {{ name }}!')
    context = Context({'name': 'Gilang'})
    rendered = template.render(context)
    return HttpResponse(rendered)


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

