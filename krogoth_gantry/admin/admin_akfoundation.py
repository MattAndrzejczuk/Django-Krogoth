from django.contrib import admin
from krogoth_gantry.models.core_models import AKFoundationAbstract, AKFoundationAngularCore, AKFoundationThemingConstant, \
    AKFoundationIndex, AKFoundationDirectives, AKFoundationConfig, AKFoundationFilters, AKFoundationThemingService, \
    AKFoundationThemingConfiguration, AKFoundationToolbar, AKFoundationQuickPanel, AKFoundationNavigation, \
    AKFoundationMain, AKFoundationRESTful

# Register your models here.

javascript = (
    '/static/fixtures/lib/codemirror.js',

    '/static/fixtures/mode/xml/xml.js',
    '/static/fixtures/mode/htmlmixed/htmlmixed.js',
    '/static/fixtures/mode/javascript/javascript.js',
    '/static/fixtures/mode/css/css.js',

    '/static/fixtures/addon/edit/matchtags.js',
    '/static/fixtures/addon/edit/closebrackets.js',
    '/static/fixtures/addon/edit/continuelist.js',
    '/static/fixtures/addon/edit/matchbrackets.js',
    '/static/fixtures/addon/edit/matchtags.js',
    '/static/fixtures/addon/edit/trailingspace.js',

    '/static/fixtures/addon/hint/javascript-hint.js',

    '/static/code_mirror_run_krogoth_core.js',
)

stylesheets = {
    'all': ('/static/fixtures.css',
            '/static/colorforth.css',
            '/static/fixtures/theme/material.css',
            '/static/fixtures/theme/midnight.css',
            '/static/fixtures/theme/twilight.css',
            '/static/fixtures/theme/dracula.css',)
}


class AKFoundationAbstractAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'ext')
    search_fields = ['first_name', 'last_name']
    class Media:
        js = javascript
        css = stylesheets


class AKFoundationAngularCoreAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'ext')

    class Media:
        js = javascript
        css = stylesheets


class AKFoundationThemingConstantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'ext')

    class Media:
        js = javascript
        css = stylesheets


class AKFoundationIndexAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'ext')

    class Media:
        js = javascript
        css = stylesheets


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
