from django.contrib import admin
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantryService, KrogothGantryDirective, \
    KrogothGantrySlaveViewController, KrogothGantryCategory, \
    AKGantryMasterViewController


class KrogothGantryMasterViewControllerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_enabled', 'title', 'icon_as_html',)
    search_fields = ['name']

    # fields = (('name', 'title', 'icon', 'category', 'is_enabled'),
    #           'module_js', 'controller_js', 'view_html', 'style_css',
    #           ('djangular_service', 'djangular_directive', 'djangular_slave_vc'))

    fieldsets = (
        ('Properties',
         {
             'fields': (('name', 'title',),
                        ('category', 'is_enabled'),
                        ('themestyle_is_enabled',),)
         }
         ),
        ('Module Editor',
         {
             'fields': ('module_js', 'themestyle',)
         }
         ),
        ('View Editor',
         {
             'fields': ('view_html',)
         }
         ),
        ('Controller Editor',
         {
             'fields': ('controller_js',)
         }
         ),
        ('Style Editor',
         {
             'fields': ('style_css',)
         }
         ),
        ('Services Directives and Slaves',
         {
             'fields': ('djangular_service', 'djangular_directive', 'djangular_slave_vc',)
         }
         ),
    )

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

            '/static/code_mirror_run_djangular_master.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '//cdn.materialdesignicons.com/1.9.32/css/materialdesignicons.min.css',
                    '/static/dracula.css',)
        }


class KrogothGantryServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name',)

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

            '/static/code_mirror_run_djangular_service.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/dracula.css',)
        }


class KrogothGantryDirectiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name',)

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

            '/static/code_mirror_run_djangular_directive.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/dracula.css',)
        }


class KrogothGantrySlaveViewControllerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name',)

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

            '/static/code_mirror_run_djangular_slave.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/dracula.css',)
        }


class KrogothGantryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)



admin.site.register(KrogothGantryCategory, KrogothGantryCategoryAdmin)

admin.site.register(KrogothGantryMasterViewController, KrogothGantryMasterViewControllerAdmin)
admin.site.register(KrogothGantryService, KrogothGantryServiceAdmin)
admin.site.register(KrogothGantryDirective, KrogothGantryDirectiveAdmin)
admin.site.register(KrogothGantrySlaveViewController, KrogothGantrySlaveViewControllerAdmin)
admin.site.register(AKGantryMasterViewController)
