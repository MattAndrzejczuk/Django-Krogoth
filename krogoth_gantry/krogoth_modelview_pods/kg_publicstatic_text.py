from django.db import models
import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from datetime import datetime
from rest_framework.decorators import api_view
from django.http import HttpResponse
import os


# - - - - - - MODELS
class KPubStaticInterfaceText(models.Model):
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
    file_name = models.CharField(max_length=100, default='index_loading_styles.txt')
    content = models.TextField(default='/* This Text doc is empty */')
    is_enabled = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True, default=timezone.now())

    def __str__(self):
        return self.unique_id


class KPublicStaticInterfaceText_UncommittedSQL(models.Model):
    document = models.ForeignKey(to=KPubStaticInterfaceText, on_delete=models.CASCADE, related_name='uncommitted_css')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def mark_static_interface_as_uncommitted(cls, unique_id):
        static_interface = KPubStaticInterfaceText.objects.get(unique_id=unique_id)
        should_mark = cls.objects.filter(document=static_interface)
        if len(should_mark) < 1:
            cls(document=static_interface).save()

    def save_to_hdd_then_destroy(self, kind):
        document_sql : KPubStaticInterfaceText = KPubStaticInterfaceText.objects.get(unique_id=self.document.unique_id)
        name_path: str = document_sql.unique_id + '.' + kind
        path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', 'textfiles', name_path)
        f = open(path_to_doc, "w")
        f.write(document_sql.content)
        f.close()
        self.delete()
# - - - - - -




# - - - - - - VIEWS
class LoadStaticText(APIView):
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
        if len(KPubStaticInterfaceText.objects.filter(unique_id=name)) > 0:
            text_doc = KPubStaticInterfaceText.objects.get(unique_id=name)
            text_response: str = text_doc.content
        else:
            return HttpResponse(name + " does not exist.", status=404)
        return HttpResponse(text_response, status=200)

class AdminEditorText(APIView):
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
        if len(KPubStaticInterfaceText.objects.filter(unique_id=name)) > 0:
            text_doc = KPubStaticInterfaceText.objects.get(unique_id=name)
            text_response: str = css_doc.content
        else:
            text_response = "THIS DOCUMENT DOES NOT EXIST."
        return HttpResponse(text_response, status=200)

    def post(self, request, name, kind):
        """
        Args:
            request:
            name:
        """
        # if name == "create_new":
        new_text: KPubStaticInterfaceText = KPubStaticInterfaceText.objects.create(
            unique_id=request.data['doc_name'],
            file_name=request.data['doc_name'] + "." + kind,
            content=request.data['content']
        )
        new_text.save()
        name_path: str = request.data['doc_name'] + '.' + kind
        f = open(os.path.join('static', 'web', 'krogoth_static_interface', 'stylesheets', name_path), "w")
        f.write(request.data['content'])
        f.close()
        return HttpResponse(new_text.unique_id + " created.", status=201)

    def patch(self, request, name):
        """Required arguments:
            name: css_doc
            request:
                request.data["content"]..

        Args:
            request:
            name:
        """
        text_doc = KPubStaticInterfaceText.objects.get(unique_id=name)
        text_doc.content = request.data["content"]
        text_doc.date_modified = datetime.now()
        text_doc.save()
        KPublicStaticInterfaceText_UncommittedSQL.mark_static_interface_as_uncommitted(unique_id=name)
        return Response({"text_doc_modified": name}, status=204)
# - - - - - -
