from django.contrib import admin
from django.forms import Textarea
from django.db import models

# Register your models here.
from krogoth_gantry.models.moho_extractor_models import IncludedHtmlMaster, IncludedJsMaster, IncludedHtmlCoreTemplate



class NgIncludedJsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_helper', )
    search_fields = ['name']

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':20,
                                                     'cols':100,
                                                     'name':'codesnippet_editable'})},
    }

    class Media:
        js = (
            '/static/fixtures/lib/codemirror.js',

            '/static/fixtures/mode/xml/xml.js',
            '/static/fixtures/mode/htmlmixed/htmlmixed.js',
            '/static/fixtures/mode/javascript/javascript.js',

            '/static/fixtures/addon/edit/matchtags.js',
            '/static/fixtures/addon/edit/closebrackets.js',
            '/static/fixtures/addon/edit/continuelist.js',
            '/static/fixtures/addon/edit/matchbrackets.js',
            '/static/fixtures/addon/edit/matchtags.js',
            '/static/fixtures/addon/edit/trailingspace.js',

            '/static/fixtures/addon/hint/javascript-hint.js',

            '/static/code_mirror_run_ngInclude.js',
        )
        css = {
            'all': ('/static/fixtures.css', '/static/colorforth.css', '/static/dracula.css',)
        }



class NgIncludedHtmlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_helper', )
    search_fields = ['name']

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':20,
                                                     'cols':100,
                                                     'name':'codesnippet_editable'})},
    }

    class Media:
        js = (
            '/static/fixtures/lib/codemirror.js',

            '/static/fixtures/mode/xml/xml.js',
            '/static/fixtures/mode/htmlmixed/htmlmixed.js',
            '/static/fixtures/mode/javascript/javascript.js',

            '/static/fixtures/addon/edit/matchtags.js',
            '/static/fixtures/addon/edit/closebrackets.js',
            '/static/fixtures/addon/edit/continuelist.js',
            '/static/fixtures/addon/edit/matchbrackets.js',
            '/static/fixtures/addon/edit/matchtags.js',
            '/static/fixtures/addon/edit/trailingspace.js',

            '/static/fixtures/addon/hint/javascript-hint.js',

            '/static/code_mirror_run_ngIncludeHtml.js',
        )
        css = {
            'all': ('/static/fixtures.css', '/static/colorforth.css', '/static/dracula.css',)
        }

admin.site.register(IncludedHtmlMaster, NgIncludedHtmlAdmin)
admin.site.register(IncludedHtmlCoreTemplate, NgIncludedHtmlAdmin)
admin.site.register(IncludedJsMaster, NgIncludedJsAdmin)