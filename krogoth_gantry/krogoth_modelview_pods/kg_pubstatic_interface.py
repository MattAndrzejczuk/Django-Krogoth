from django.db import models
import uuid
import codecs
import datetime
from django.utils import timezone


from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from datetime import datetime
# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.urls import path




# - - - - - - MODELS
class KPubStaticInterfaceCSS(models.Model):
    """KPubStaticInterfaceCSS

    By default, sets editable=False, blank=True, unique=False.

    Required arguments:

    unique_id
        Name for unique document

    Optional arguments:

    file_name
        Don't touch this property

    content
        the css code itself

    is_enabled
        If set to True, uppercase the alpha characters (default: False)

    pub_date
        automatically generated

    date_modified
        automatically generated

    Example

    ``

        new_css = KPubStaticInterfaceCSS.objects.create(

                unique_id="my_file",
                file_name="my_file.css",
                content="/ ** /"

            )

    ``
    """

    unique_id = models.CharField(primary_key=True, max_length=25)
    file_name = models.CharField(max_length=100, default='index_loading_styles.css')
    content = models.TextField(default='/* This CSS doc is empty */')
    is_enabled = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True, default=timezone.now())

    def __str__(self):
        return self.unique_id


class KPublicStaticInterfaceCSS_UncommittedSQL(models.Model):
    document = models.ForeignKey(to=KPubStaticInterfaceCSS, on_delete=models.CASCADE, related_name='uncommitted_css')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def mark_static_interface_as_uncommitted(cls, unique_id):
        static_interface = KPubStaticInterfaceCSS.objects.get(unique_id=unique_id)
        should_mark = cls.objects.filter(document=static_interface)
        if len(should_mark) < 1:
            cls(document=static_interface).save()

    def save_to_hdd_then_destroy(self):
        document_sql : KPubStaticInterfaceCSS = KPubStaticInterfaceCSS.objects.get(unique_id=self.document.unique_id)
        name_path: str = document_sql.unique_id + '.css'
        path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', 'stylesheets', name_path)
        f = open(path_to_doc, "w")
        f.write(document_sql.content)
        f.close()
        self.delete()
# - - - - - -


@api_view(['GET'])
def load_static_css_readonly(request, unique_id):
    """
    Public endpoint for readonly, should only be used in  dev mode, production mode this
    should  come from the static files like most other  normal  Django apps.
          static/web/krogoth_static_interface/stylesheets/{unique_id}.css

    http://HOST_NAME/global_static_interface/load_static_css_readonly/{ UNIQUE_ID }

    """
    document_sql : KPubStaticInterfaceCSS = KPubStaticInterfaceCSS.objects.filter(unique_id=unique_id).first()
    if document_sql is not None:
        return HttpResponse(document_sql.content, content_type='text/css', status=200)
    else:
        return HttpResponse('', content_type='text/css', status=404)


# - - - - - - VIEWS
# class LoadStaticCSS(APIView):
#     """LoadStaticCSS
#
#     returns pure CSS code to the client.
#     """
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request, name):
#         """
#         Required arguments:
#             name
#                 KPubStaticInterfaceCSS.unique_id
#         """
#         text_response: str
#         if len(KPubStaticInterfaceCSS.objects.filter(unique_id=name)) > 0:
#             css_doc = KPubStaticInterfaceCSS.objects.get(unique_id=name)
#             text_response: str = css_doc.content
#         else:
#             return HttpResponse(name + " does not exist.", status=404)
#         return HttpResponse(text_response, status=200)

class AdminEditorCSS(APIView):
    """LoadStaticCSS

    returns pure CSS code to the client.

    Required arguments:

        file_ext
            What kind of file

        unique_id
            primary key

        content
            content of file

    Optional arguments:

    is_enabled
        blocks the document from being loaded even with URL

    """
    permission_classes = (permissions.AllowAny,)
    def get(self, request, name):
        """
        Required arguments:
            name: The name could be saved as CUSTOM.TXT to `static/web/krogoth_static_interface/stylesheets/NAME_ARG.CSS`
        Response:
            KPubStaticInterfaceCSS's content in for use in HTML src paths.
        """
        text_response: str
        if len(KPubStaticInterfaceCSS.objects.filter(unique_id=name)) > 0:
            css_doc = KPubStaticInterfaceCSS.objects.get(unique_id=name)
            text_response: str = css_doc.content
        else:
            text_response = "THIS DOCUMENT DOES NOT EXIST."
        return HttpResponse(text_response, status=200)

    def post(self, request, name):
        """
        Args:
            request:
            name:
        """
        # if name == "create_new":
        new_css: KPubStaticInterfaceCSS = KPubStaticInterfaceCSS.objects.create(
            unique_id=request.data['doc_name'],
            file_name=request.data['doc_name'] + ".css",
            content=request.data['content']
        )
        new_css.save()
        name_path: str = request.data['doc_name'] + '.css'
        f = open(os.path.join('static', 'web', 'krogoth_static_interface', 'stylesheets', name_path), "w")
        f.write(request.data['content'])
        f.close()
        return HttpResponse(new_css.unique_id + " created.", status=201)

    def patch(self, request, name):
        """Required arguments:
            name: css_doc
            request:
                request.data["content"]..

        Args:
            request:
            name:
        """
        css_doc = KPubStaticInterfaceCSS.objects.get(unique_id=name)
        css_doc.content = request.data["content"]
        css_doc.date_modified = datetime.now()
        css_doc.save()
        KPublicStaticInterfaceCSS_UncommittedSQL.mark_static_interface_as_uncommitted(unique_id=name)
        return Response({"css_doc_modified": name}, status=204)
# - - - - - -



class KPubStaticTextDocument(models.Model):
    """KPubStaticTextDocument

    Can be almost any text based document, and loaded as HTML, JS, etc...

    Required arguments:

        file_ext
            What kind of file

        unique_id
            primary key

        content
            content of file

    Optional arguments:

    is_enabled
        blocks the document from being loaded even with URL
    """
    unique_id = models.CharField(primary_key=True, max_length=25)
    file_name = models.CharField(max_length=100, default='index_loading_styles.css')
    content = models.TextField(default='/* This CSS doc is empty */')
    is_enabled = models.BooleanField(default=True)
    file_ext = models.CharField(max_length=25, default=".css")

    pub_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True, default=timezone.now())

    def __str__(self):
        return self.unique_id

class AdminEditorTextDocument(APIView):
    """AdminEditorTextDocument

    read, create, and edit KPubStaticTextDocuments. For admin users only.

    .. code-block:: python

        path('admin_editor_text/<str:name>/',
        AdminEditorTextDocument.as_view()),
    """

    permission_classes = (permissions.AllowAny,)
    def get(self, request, name):
        """
        Required arguments:
            name: The name could be saved as CUSTOM.TXT to `static/web/krogoth_static_interface/textfiles/NAME_ARG.TXT`
        Response:
            KPubStaticTextDocument's content in for use in HTML src paths.
        """
        text_response: str
        if len(KPubStaticTextDocument.objects.filter(unique_id=name)) > 0:
            txt_doc = KPubStaticTextDocument.objects.get(unique_id=name)
            text_response: str = txt_doc.content
        else:
            text_response = "THIS DOCUMENT DOES NOT EXIST."
        return HttpResponse(text_response, status=200)


    def post(self, request, name):
        """
        Required arguments:
            name: The name could be saved as CUSTOM.TXT to `static/web/krogoth_static_interface/textfiles/NAME_ARG.TXT`
        Response:
            KPubStaticTextDocument's unique_id and 201 Created

        POST body:
            {
                "file_ext": ".html"
                "doc_name": "unique_name"
                "text_code": "Lots of source code here"
            }
        """
        if name == "create_new":
            new_css = KPubStaticTextDocument.objects.create(
                file_ext=request.data('file_ext'),
                unique_id=request.data('doc_name'),
                file_name=request.data('doc_name') + request.data('file_ext'),
                content=request.data('text_code')
            )
            new_css.save()
            with open("static/web/krogoth_static_interface/stylesheets/" + name + ".css") as documentcontents:
                documentcontents.write(request.data('text_code'))
                documentcontents.close()
            return HttpResponse(new_css.unique_id + " created.", status=201)

    def patch(self, request, name):
        """
        Required arguments:
            name: The name of the existing file to modify.
        Response 204 no content:
            {
                "text_doc_modified": NAME_OF_FILE.TXT
            }

        PATCH body:
            {
                "file_ext": ".html"
                "doc_name": "unique_name"
                "text_code": "Lots of source code here"
            }
        """
        text_doc = KPubStaticTextDocument.objects.get(unique_id=name)
        text_doc.content = request.data["content"]
        text_doc.date_modified = datetime.now()
        text_doc.save()
        return Response({"text_doc_modified": name}, status=204)





@api_view(['GET'])
def api_index(request):
    """
    Just a placeholder index.
    http://HOST_NAME/global_static_interface/
    """
    examples: [str] = [
        'GET     /global_static_interface/load_static_css_readonly/<NAME_OF_CSS_DOC>/',
        'GET     /global_static_interface/admin_editor_css/<NAME_OF_CSS_DOC>/',
        'PATCH   /global_static_interface/admin_editor_css/<NAME_OF_CSS_DOC>/',
        'POST    /global_static_interface/admin_editor_css/create_new/',
        'GET     /global_static_interface/save_sqldb_to_filesystem_css/<NAME_OF_CSS_DOC>',
        'GET     /global_static_interface/save_filesystem_to_sqldb_css/<NAME_OF_CSS_DOC>',
    ]
    return Response({"catalog": examples})

import os, codecs

@api_view(['GET'])
def save_sqldb_to_filesystem_css(request, unique_id):
    """

    Copies the DB contents, saves them to
          static/web/krogoth_static_interface/stylesheets/{unique_id}.css

    http://HOST_NAME/global_static_interface/save_sqldb_to_filesystem_css/{ UNIQUE_ID }

    """
    name_path : str = unique_id + '.css'
    document_sql : KPubStaticInterfaceCSS = KPubStaticInterfaceCSS.objects.get(unique_id=unique_id)
    path_to_doc : str = os.path.join('static', 'web', 'krogoth_static_interface', 'stylesheets', name_path)
    text_file = open(path_to_doc, "w")
    text_file.write(document_sql.content)
    text_file.close()
    tracker : KPublicStaticInterfaceCSS_UncommittedSQL = KPublicStaticInterfaceCSS_UncommittedSQL.objects.get(document=document_sql)
    tracker.save_to_hdd_then_destroy()
    completed_work: [str] = [
        document_sql.unique_id,
        path_to_doc,
        'Database copy saved into filesystem.',
    ]
    return Response({"completed_work": completed_work})


@api_view(['GET'])
def save_filesystem_to_sqldb_css(request, unique_id):
    """

    Copies the DB contents, saves them to
          static/web/krogoth_static_interface/stylesheets/{unique_id}.css

    http://HOST_NAME/global_static_interface/save_filesystem_to_sqldb_css/{ UNIQUE_ID }

    """
    name_path : str = unique_id + '.css'
    document_sql : KPubStaticInterfaceCSS = KPubStaticInterfaceCSS.objects.get(unique_id=unique_id)
    path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', 'stylesheets', name_path)
    unsaved_work = KPublicStaticInterfaceCSS_UncommittedSQL.objects.filter(document=document_sql)
    if len(unsaved_work) > 1:
        return Response({"error":"YOU HAVE UNSAVED WORK ON SQL FOR " + unique_id}, status=401)
    else:
        document_sql.content = codecs.open(path_to_doc, 'r').read()
        document_sql.save()
        completed_work: [str] = [
            document_sql.unique_id,
            path_to_doc,
            'Database copy saved into filesystem.',
        ]
        return Response({"completed_work": completed_work})




urlpatterns = [
    path('', api_index),
    path('load_static_css_readonly/<str:unique_id>/', load_static_css_readonly),
    path('admin_editor_css/<str:name>/', AdminEditorCSS.as_view()),

# create_new_text_doc

    path('save_sqldb_to_filesystem_css/<str:unique_id>/', save_sqldb_to_filesystem_css, name="Save SQL And Store Into HDD"),
    path('save_filesystem_to_sqldb_css/<str:unique_id>/', save_filesystem_to_sqldb_css, name="Save HDD And Store Into SQL"),
]

