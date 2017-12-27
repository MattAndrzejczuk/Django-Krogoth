from django.contrib import admin
from krogoth_core.models import AKFoundationAbstract, AKFoundationAngularCore, AKFoundationThemingConstant, \
    AKFoundationIndex, AKFoundationDirectives, AKFoundationConfig, AKFoundationFilters, AKFoundationThemingService, \
    AKFoundationThemingConfiguration, AKFoundationToolbar, AKFoundationQuickPanel, AKFoundationNavigation, \
    AKFoundationMain, AKFoundationRESTful
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

            '/static/code_mirror_run_krogoth_core.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/codemirror/theme/material.css',
                    '/static/codemirror/theme/midnight.css',
                    '/static/codemirror/theme/twilight.css',
                    '/static/codemirror/theme/dracula.css',)
        }

class AKFoundationAngularCoreAdmin(admin.ModelAdmin):
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

            '/static/code_mirror_run_krogoth_core.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/codemirror/theme/material.css',
                    '/static/codemirror/theme/midnight.css',
                    '/static/codemirror/theme/twilight.css',
                    '/static/codemirror/theme/dracula.css',)
        }

class AKFoundationThemingConstantAdmin(admin.ModelAdmin):
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

            '/static/code_mirror_run_krogoth_core.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/codemirror/theme/material.css',
                    '/static/codemirror/theme/midnight.css',
                    '/static/codemirror/theme/twilight.css',
                    '/static/codemirror/theme/dracula.css',)
        }

class AKFoundationIndexAdmin(admin.ModelAdmin):
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

            '/static/code_mirror_run_krogoth_core.js',
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

admin.site.register(AKFoundationAngularCore, AKFoundationAngularCoreAdmin)
admin.site.register(AKFoundationThemingConstant, AKFoundationThemingConstantAdmin)
admin.site.register(AKFoundationIndex, AKFoundationIndexAdmin)

admin.site.register(AKFoundationDirectives, AKFoundationAbstractAdmin)
admin.site.register(AKFoundationConfig, AKFoundationAbstractAdmin)
admin.site.register(AKFoundationFilters, AKFoundationAbstractAdmin)
admin.site.register(AKFoundationThemingService, AKFoundationAbstractAdmin)

admin.site.register(AKFoundationThemingConfiguration, AKFoundationAbstractAdmin)
admin.site.register(AKFoundationToolbar, AKFoundationAbstractAdmin)
admin.site.register(AKFoundationQuickPanel, AKFoundationAbstractAdmin)
admin.site.register(AKFoundationNavigation, AKFoundationAbstractAdmin)

admin.site.register(AKFoundationMain, AKFoundationAbstractAdmin)
admin.site.register(AKFoundationRESTful, AKFoundationAbstractAdmin)
