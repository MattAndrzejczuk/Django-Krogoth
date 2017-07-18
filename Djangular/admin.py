from django.contrib import admin
from Djangular.models import DjangularMasterViewController, DjangularService, DjangularDirective, \
    DjangularSlaveViewController, DjangularIcon, DjangularCategory






class DjangularMasterViewControllerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
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

            '/static/code_mirror_run_djangular_master.js',
        )
        css = {
            'all': ('/static/codemirror.css',
                    '/static/colorforth.css',
                    '/static/dracula.css',)
        }

class DjangularServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
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

class DjangularDirectiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
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

class DjangularSlaveViewControllerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
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


class DjangularIconAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

class DjangularCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


admin.site.register(DjangularIcon, DjangularIconAdmin)
admin.site.register(DjangularCategory, DjangularCategoryAdmin)


admin.site.register(DjangularMasterViewController, DjangularMasterViewControllerAdmin)
admin.site.register(DjangularService, DjangularServiceAdmin)
admin.site.register(DjangularDirective, DjangularDirectiveAdmin)
admin.site.register(DjangularSlaveViewController, DjangularSlaveViewControllerAdmin)