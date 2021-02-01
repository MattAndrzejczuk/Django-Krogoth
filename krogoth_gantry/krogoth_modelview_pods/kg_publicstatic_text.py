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

    unique_id = models.CharField(primary_key=True, max_length=70)
    file_name = models.CharField(max_length=50, default='index_loading_styles.txt')
    file_kind = models.CharField(max_length=20, default='txt')
    content = models.TextField(default='/* This Text doc is empty */')
    is_enabled = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True, default=timezone.now())

    def __str__(self):
        return self.unique_id


class KPublicStaticInterfaceText_UncommittedSQL(models.Model):
    document = models.ForeignKey(to=KPubStaticInterfaceText, on_delete=models.CASCADE, related_name='uncommitted_text')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def mark_static_interface_as_uncommitted(cls, unique_id):
        static_interface = KPubStaticInterfaceText.objects.get(unique_id=unique_id)
        should_mark = cls.objects.filter(document=static_interface)
        if len(should_mark) < 1:
            cls(document=static_interface).save()

    def save_to_hdd_then_destroy(self, full_path):
        document_sql : KPubStaticInterfaceText = KPubStaticInterfaceText.objects.get(unique_id=self.document.unique_id)
        # name_path: str = document_sql.unique_id + '.' + kind
        # path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', 'textfiles', name_path)
        f = open(full_path, "w")
        f.write(document_sql.content)
        f.close()
        self.delete()
# - - - - - -




# - - - - - - VIEWS


@api_view(['GET'])
def load_static_text_readonly(request, unique_id, file_kind):
    """
    Public endpoint for readonly, should only be used in  dev mode, production mode this
    should  come from the static files like most other  normal  Django apps.
          static/web/krogoth_static_interface/stylesheets/{unique_id}.css

    http://HOST_NAME/global_static_interface/load_static_text_readonly/{ FILE_EXT }/{ UNIQUE_ID }

    """
    document_sql : KPubStaticInterfaceText = KPubStaticInterfaceText.objects.filter(unique_id=unique_id).first()
    if document_sql is not None:
        return HttpResponse(document_sql.content, content_type='text/'+file_kind, status=200)
    else:
        return HttpResponse('', content_type='text/css', status=404)


@api_view(['GET'])
def get_uncommitted_docs(request):
    """
    Get all uncommitted docs which are in SQL, but are  not yet physically saved to the HDD at the
    path /static/web/krogoth_static_interface/HTML/document.html

    http://HOST_NAME/global_static_interface/load_static_text_readonly/{ UNIQUE_ID }/html

    """
    uncommited_docs : [KPublicStaticInterfaceText_UncommittedSQL] = KPublicStaticInterfaceText_UncommittedSQL.objects.all()
    reply = {}
    reply['total'] : int = len(uncommited_docs)
    reply['docs'] : [{str:str}] = []
    for doc in uncommited_docs:
        name_path: str = doc.document.unique_id + '.' + doc.document.file_kind
        path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', doc.document.file_kind, name_path)
        a_document = {}
        a_document['unique_id'] = doc.document.unique_id
        a_document['path_to_doc'] = '/' + path_to_doc
        a_document['file_kind'] = doc.document.file_kind
        a_document['date_modified'] = doc.pub_date.__str__()
        reply['docs'].append(a_document)
    return Response(reply, content_type='application/json', status=200)



class AdminEditorTextDetail(APIView):
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



    def post(self, request):
        """
        Public endpoint for readonly, should only be used in  dev mode, production mode this
        should  come from the static files like most other  normal  Django apps.
              static/web/krogoth_static_interface/stylesheets/{unique_id}.css

        http://HOST_NAME/global_static_interface/create_new_text_doc
        """
        """
            Args:
                request: POST
                body: {
                    'doc_name': 'test',
                    'doc_kind': 'html',
                    'content': 'CODE'
                }
        """
        doc_ext : str = str(request.data['doc_kind']).upper()
        new_text: KPubStaticInterfaceText = KPubStaticInterfaceText.objects.create(
            unique_id=request.data['doc_name'],
            file_kind=doc_ext,
            file_name=request.data['doc_name'] + "." + doc_ext,
            content=request.data['content']
        )
        new_text.save()
        name_path: str = request.data['doc_name'] + '.' + doc_ext
        save_folder: str = os.path.join('static', 'web', 'krogoth_static_interface', doc_ext)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        f = open(os.path.join('static', 'web', 'krogoth_static_interface', doc_ext, name_path), "w")
        f.write(request.data['content'])
        f.close()
        return HttpResponse(new_text.file_name + " created.", status=201)

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

@api_view(['GET'])
def save_sqldb_to_filesystem_text(request, unique_id):
    """

    Copies the DB contents, saves them to
          static/web/krogoth_static_interface/{file_kind}/{unique_id}.css

    http://HOST_NAME/global_static_interface/save_sqldb_to_filesystem_text/{ UNIQUE_ID }

    """
    document_sql: KPubStaticInterfaceText = KPubStaticInterfaceText.objects.get(unique_id=unique_id)
    name_path : str = unique_id + '.' + document_sql.file_kind
    path_to_doc : str = os.path.join('static', 'web', 'krogoth_static_interface', document_sql.file_kind, name_path)
    text_file = open(path_to_doc, "w")
    text_file.write(document_sql.content)
    text_file.close()
    tracker : KPublicStaticInterfaceText_UncommittedSQL = KPublicStaticInterfaceText_UncommittedSQL.objects.get(document=document_sql)
    tracker.save_to_hdd_then_destroy(full_path=path_to_doc)
    completed_work: [str] = [
        document_sql.unique_id,
        path_to_doc,
        'KPubStaticInterfaceText Database copy saved into filesystem.',
    ]
    return Response({"completed_work": completed_work})

from django.urls import path

urlpatterns = [
    # get_uncommitted_docs
    path('admin_editor_text/<str:name>/', AdminEditorText.as_view(), name="POST Create New Text Document"),
    path('admin_editor_text/', AdminEditorTextDetail.as_view(), name="POST Create New Text Document"),
    path('admin_editor_text/<str:file_kind>/<str:unique_id>/', load_static_text_readonly, name="GET Static Document"),
    path('get_uncommitted_docs/', get_uncommitted_docs, name="GET uncommitted docs that are only in SQL."),

    path('save_sqldb_to_filesystem_text/<str:unique_id>/', save_sqldb_to_filesystem_text, name="Save SQL And Store Into HDD"),
    # path('save_filesystem_to_sqldb_css/<str:unique_id>/', save_filesystem_to_sqldb_css, name="Save HDD And Store Into SQL"),

]