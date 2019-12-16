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
            '/static/codemirror/lib/codemirror.js',

            '/static/codemirror/mode/xml/xml.js',
            '/static/codemirror/mode/htmlmixed/htmlmixed.js',
            '/static/codemirror/mode/javascript/javascript.js',

            '/static/codemirror/addon/edit/matchtags.js',
            '/static/codemirror/addon/edit/closebrackets.js',
            '/static/codemirror/addon/edit/continuelist.js',
            '/static/codemirror/addon/edit/matchbrackets.js',
            '/static/codemirror/addon/edit/matchtags.js',
            '/static/codemirror/addon/edit/trailingspace.js',

            '/static/codemirror/addon/hint/javascript-hint.js',

            '/static/code_mirror_run_ngInclude.js',
        )
        css = {
            'all': ('/static/codemirror.css', '/static/colorforth.css', '/static/dracula.css',)
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
            '/static/codemirror/lib/codemirror.js',

            '/static/codemirror/mode/xml/xml.js',
            '/static/codemirror/mode/htmlmixed/htmlmixed.js',
            '/static/codemirror/mode/javascript/javascript.js',

            '/static/codemirror/addon/edit/matchtags.js',
            '/static/codemirror/addon/edit/closebrackets.js',
            '/static/codemirror/addon/edit/continuelist.js',
            '/static/codemirror/addon/edit/matchbrackets.js',
            '/static/codemirror/addon/edit/matchtags.js',
            '/static/codemirror/addon/edit/trailingspace.js',

            '/static/codemirror/addon/hint/javascript-hint.js',

            '/static/code_mirror_run_ngIncludeHtml.js',
        )
        css = {
            'all': ('/static/codemirror.css', '/static/colorforth.css', '/static/dracula.css',)
        }

admin.site.register(IncludedHtmlMaster, NgIncludedHtmlAdmin)
admin.site.register(IncludedHtmlCoreTemplate, NgIncludedHtmlAdmin)
admin.site.register(IncludedJsMaster, NgIncludedJsAdmin)