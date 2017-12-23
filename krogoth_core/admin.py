from django.contrib import admin
from krogoth_core.models import AKFoundationAbstract
# Register your models here.



class AKFoundationAbstractAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'ext')
    class Media:
        js = (
            '/static/codemirror/lib/codemirror.js',

            '/static/codemirror/mode/xml/xml.js',
            '/static/codemirror/mode/htmlmixed/htmlmixed.js',
            '/static/codemirror/mode/javascript/javascript.js',
            '/static/codemirror/mode/css/css.js',

            '/static/codemirror/addon/edit/matchtags.js',
            '/static/codemirror/addon/edit/closebrackets.js',
            '/static/codemirror/addon/edit/continuelist.js',
            '/static/codemirror/addon/edit/matchbrackets.js',
            '/static/codemirror/addon/edit/matchtags.js',
            '/static/codemirror/addon/edit/trailingspace.js',

            '/static/codemirror/addon/hint/javascript-hint.js',

            '/moho_extractor/NgIncludedJs/?name=codemirror_krogoth_core',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/codemirror/theme/material.css',
                    '/static/codemirror/theme/midnight.css',
                    '/static/codemirror/theme/twilight.css',
                    '/static/codemirror/theme/dracula.css',)
        }

admin.site.register(AKFoundationAbstract, AKFoundationAbstractAdmin)