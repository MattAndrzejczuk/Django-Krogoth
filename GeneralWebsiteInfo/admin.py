from django.contrib import admin
from GeneralWebsiteInfo.models import WebsiteColorTheme, WebsiteLayout, \
    NavigationBar, BootScreenLoader
from django.forms import TextInput, Textarea
from django.db import models


# GeneralWebsiteInfo



class WebsiteColorThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'css_code', 'enabled',)


class WebsiteLayoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'enabled',)


class NavigationBarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'logo_html_code', 'enabled',)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':50,
                                                     'cols':300,
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

            '/static/codemirror_run.js',
        )
        css = {
            'all': ('/static/codemirror.css', '/static/colorforth.css', '/static/dracula.css',)
        }


class BootScreenLoaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'width', 'main_background_color', 'logo_background_color', 'font_color',)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':50,
                                                     'cols':300,
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

            '/static/codemirror_run.js',
        )
        css = {
            'all': ('/static/codemirror.css', '/static/colorforth.css', '/static/dracula.css',)
        }








admin.site.register(WebsiteColorTheme, WebsiteColorThemeAdmin)
admin.site.register(WebsiteLayout, WebsiteLayoutAdmin)
admin.site.register(NavigationBar, NavigationBarAdmin)
admin.site.register(BootScreenLoader, BootScreenLoaderAdmin)