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

class LoadStaticCSS(APIView):
    """LoadStaticCSS

    returns pure CSS code to the client.
    """
    permission_classes = (permissions.AllowAny,)
    def get(self, request, name):
        """
        Required arguments:
            name
                KPubStaticInterfaceCSS.unique_id
        """
        text_response: str
        if len(KPubStaticInterfaceCSS.objects.filter(unique_id=name)) > 0:
            css_doc = KPubStaticInterfaceCSS.objects.get(unique_id=name)
            text_response: str = css_doc.content
        else:
            return HttpResponse(name + " does not exist.", status=404)
        return HttpResponse(text_response, status=200)

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
        if name == "create_new":
            new_css = KPubStaticInterfaceCSS.objects.create(
                unique_id=request.data('doc_name'),
                file_name=request.data('doc_name') + ".css",
                content=request.data('css_code')
            )
            new_css.save()
            with open("static/web/krogoth_static_interface/stylesheets/" + name + ".css") as documentcontents:
                documentcontents.write(request.data('css_code'))
                documentcontents.close()
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
        return Response({"css_doc_modified": name}, status=204)








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





@api_view(['GET', 'POST'])
def api_index(request):
    """
    Just a placeholder index.
    http://HOST_NAME/global_static_interface/
    """
    examples: [str] = [
        'load_static_css/<str:name>/ LoadStaticCSS',
        'admin_editor_css/<str:name>/ AdminEditorCSS',
        'admin_editor_text/<str:name>/ AdminEditorTextDocument',
    ]
    return Response({"catalog": examples})




from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('', api_index),
    path('load_static_css/<str:name>/', LoadStaticCSS.as_view()),
    path('admin_editor_css/<str:name>/', AdminEditorCSS.as_view()),
    path('admin_editor_text/<str:name>/', AdminEditorTextDocument.as_view()),
]

