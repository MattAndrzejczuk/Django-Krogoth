from django.contrib import admin
from krogoth_gantry.models import krogoth_gantryMasterViewController, krogoth_gantryService, krogoth_gantryDirective, \
    krogoth_gantrySlaveViewController, krogoth_gantryIcon, krogoth_gantryCategory






class krogoth_gantryMasterViewControllerAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_enabled', 'title', 'name', )
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

class krogoth_gantryServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', )
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

class krogoth_gantryDirectiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', )
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

class krogoth_gantrySlaveViewControllerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', )
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


class krogoth_gantryIconAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

class krogoth_gantryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


admin.site.register(krogoth_gantryIcon, krogoth_gantryIconAdmin)
admin.site.register(krogoth_gantryCategory, krogoth_gantryCategoryAdmin)


admin.site.register(krogoth_gantryMasterViewController, krogoth_gantryMasterViewControllerAdmin)
admin.site.register(krogoth_gantryService, krogoth_gantryServiceAdmin)
admin.site.register(krogoth_gantryDirective, krogoth_gantryDirectiveAdmin)
admin.site.register(krogoth_gantrySlaveViewController, krogoth_gantrySlaveViewControllerAdmin)