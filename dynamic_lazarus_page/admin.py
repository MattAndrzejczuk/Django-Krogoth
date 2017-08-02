from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models




# Register your models here.
from dynamic_lazarus_page.models import FuseAppComponent, AngularFuseApplication, NgIncludedHtml, NgIncludedJs



# class AngularFuseApplicationAdmin(admin.ModelAdmin):
#
#     list_display = ('id', 'name', 'category',)
#
#     formfield_overrides = {
#         models.TextField: {'widget': Textarea(attrs={'rows':20,
#                                                      'cols':100,
#                                                      'name':'codesnippet_editable'})},
#     }
#
#     class Media:
#         js = (
#             '/static/codemirror/lib/codemirror.js',
#
#             '/static/codemirror/mode/xml/xml.js',
#             '/static/codemirror/mode/htmlmixed/htmlmixed.js',
#             '/static/codemirror/mode/javascript/javascript.js',
#
#             '/static/codemirror/addon/edit/matchtags.js',
#             '/static/codemirror/addon/edit/closebrackets.js',
#             '/static/codemirror/addon/edit/continuelist.js',
#             '/static/codemirror/addon/edit/matchbrackets.js',
#             '/static/codemirror/addon/edit/matchtags.js',
#             '/static/codemirror/addon/edit/trailingspace.js',
#
#             '/static/codemirror/addon/hint/javascript-hint.js',
#
#             '/static/codemirror_run.js',
#         )
#         css = {
#             'all': ('/static/codemirror.css', '/static/colorforth.css', '/static/dracula.css',)
#        }




# class FuseAppComponentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name','type','parent_app','contents',)



# class FuseAppComponentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name','type','parent_app','contents',)



class NgIncludedJsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_helper', )

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


# admin.site.register(AngularFuseApplication, AngularFuseApplicationAdmin)
# admin.site.register(FuseAppComponent, FuseAppComponentAdmin)
admin.site.register(NgIncludedHtml, NgIncludedHtmlAdmin)
admin.site.register(NgIncludedJs, NgIncludedJsAdmin)