from django.db import models
import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from datetime import datetime
from rest_framework.decorators import api_view
from django.http import HttpResponse
import os, codecs


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

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#
# from krogoth_gantry.models.gantry_models import KrogothGantryMasterViewController, AKFoundationAbstract

from krogoth_gantry.models import KrogothGantryMasterViewController, AKFoundationAbstract

@api_view(['GET'])
def load_static_text_readonly(request, filename):
    """
    Public endpoint for readonly, should only be used in  dev mode, production mode this
    should  come from the static files like most other  normal  Django apps.
          static/web/krogoth_static_interface/{file_kind}/{unique_id}.{file_kind}

    http://localhost:8000/global_static_text/load_static_text_readonly/index.module.js/

    """
    # unique_name = str(request.GET['unique_name'])
    # js = AKFoundationAbstract.objects.get(unique_name=unique_name)
    # ct = 'application/javascript'

    document_sql: KPubStaticInterfaceText = KPubStaticInterfaceText.objects.filter(file_name=filename).first()


    injection = "console.log('DEPENDENCY CALLED: " + filename + "');var vm = this"
    body = document_sql.content.replace("var vm = this", injection)

    if filename == 'index.module.js':
        all_djangular = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
        my_apps = ''
        for application in all_djangular:
            my_apps += ("\t\t\t'app." + application.name + "',\n")
        body = body.replace('/*|#apps#|*/', my_apps)

    print(OKBLUE + "filename : " + OKGREEN + filename + ENDC)
    mime = document_sql.file_kind
    if document_sql is not None:
        if mime.upper() == 'JS' or mime.upper() == 'ES6':
            mime = 'javascript'
        print(OKBLUE + "filename : " + OKGREEN + filename + ENDC)
        return HttpResponse(content_type='text/'+mime, content=body)
    else:
        print(FAIL + "filename : " + WARNING + filename + ENDC)
        return HttpResponse(content_type='text/'+mime, content=body)


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
        name_path: str = doc.document.file_name
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
def save_sqldb_to_filesystem_text(request, file_name):
    """

    Copies the DB contents, saves them to
          static/web/krogoth_static_interface/{file_kind}/{unique_id}.css

    http://HOST_NAME/global_static_interface/save_sqldb_to_filesystem_text/{ UNIQUE_ID }

    """
    document_sql: KPubStaticInterfaceText = KPubStaticInterfaceText.objects.get(file_name=file_name)
    name_path : str = file_name
    path_to_doc : str = os.path.join('static', 'web', 'krogoth_static_interface', document_sql.file_kind, name_path)
    text_file = open(path_to_doc, "w")
    text_file.write(document_sql.content)
    text_file.close()
    tracker : KPublicStaticInterfaceText_UncommittedSQL = KPublicStaticInterfaceText_UncommittedSQL.objects.filter(document=document_sql)
    if tracker.count() > 0:
        KPublicStaticInterfaceText_UncommittedSQL.objects.get(document=document_sql).save_to_hdd_then_destroy(full_path=path_to_doc)
    completed_work: [str] = [
        document_sql.unique_id,
        path_to_doc,
        'KPubStaticInterfaceText Database copy saved into filesystem.',
    ]
    return Response({"completed_work": completed_work})




@api_view(['GET'])
def save_filesystem_to_sqldb_text(request, file_name):
    """

    Copies the DB contents, saves them to
          static/web/krogoth_static_interface/{FILE_EXT}/{unique_id}.{FILE_EXT}

    http://HOST_NAME/global_static_text/save_filesystem_to_sqldb_text/{ UNIQUE_ID }

    """
    document_sql : KPubStaticInterfaceText
    try:
        document_sql = KPubStaticInterfaceText.objects.get(file_name=file_name)
    except:
        split_file = file_name.split('.')
        doc_ext = str(split_file[len(split_file) - 1]).upper()
        path_to_file = os.path.join('static', 'web', 'krogoth_static_interface', doc_ext, file_name)
        f = codecs.open(path_to_file, 'r').read()
        new = KPubStaticInterfaceText(
            unique_id=file_name.replace("."+doc_ext, ""),
            file_name=file_name,
            file_kind=str(doc_ext).upper(),
            content=f,
            pub_date=datetime.now()
        )
        new.save()
        return Response({"result": "Not in DB."}, status=403)
    name_path: str = file_name
    path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', document_sql.file_kind, name_path)
    unsaved_work = KPublicStaticInterfaceText_UncommittedSQL.objects.filter(document=document_sql)
    if len(unsaved_work) > 1:
        return Response({"error":"YOU HAVE UNSAVED WORK ON SQL FOR " + file_name}, status=401)
    else:
        document_sql.content = codecs.open(path_to_doc, 'r').read()
        document_sql.save()
        completed_work: [str] = [
            document_sql.unique_id,
            path_to_doc,
            'Database copy saved into filesystem.',
        ]
        return Response({"completed_work": completed_work})

from .filesystem_to_db import KSI_Processor


@api_view(['GET', 'POST'])
def saveall_filesystem_to_sqldb_text(request):
    """

    Copies the DB contents, saves them to
          static/web/krogoth_static_interface/{FILE_EXT}/{unique_id}.{FILE_EXT}

    http://HOST_NAME/global_static_text/saveall_filesystem_to_sqldb_text/

        request: GET   - nothing, no params or body

        request: POST  -
            body: {
                'paths_to_include': ['JS','HTML']
            }
    """

    outcome = KSI_Processor.run_task_saveall_filesystem_to_sql()
    if outcome['completed_work'] == 'failed':
        return Response(outcome, status=403)
    else:
        return Response(outcome, status=200)

# TODO REMOVE THIS EXTRA VIEW, MIGHT NOT NEED ANYMORE
@api_view(['GET'])
def save_filesystem_to_sqldb_text_new(request, unique_id, doc_kind):
    """

    Copies the DB contents, saves them to
          static/web/krogoth_static_interface/stylesheets/{unique_id}.css

    http://HOST_NAME/global_static_interface/save_filesystem_to_sqldb_css/{ UNIQUE_ID }

    """
    doc_kind_formated : str = str(doc_kind).upper()
    # document_sql : KPubStaticInterfaceText = KPubStaticInterfaceText.objects.get_or_create(
    #     unique_id=unique_id,
    #     file_name=unique_id + '.' + doc_kind,
    #     file_kind=doc_kind
    # )

    name_path: str = unique_id + '.' + doc_kind_formated
    document_sql = KPubStaticInterfaceText.objects.filter(unique_id=unique_id, file_kind=doc_kind_formated)
    unique_id = unique_id.replace('-', '.')
    path_to_doc = os.path.join('static', 'web', 'krogoth_static_interface', doc_kind_formated, name_path.replace('-', '.'))
    if len(document_sql) > 0:

        unsaved_work = KPublicStaticInterfaceText_UncommittedSQL.objects.filter(document=document_sql)
        if len(unsaved_work) > 1:
            return Response({"error":"YOU HAVE UNSAVED WORK ON SQL FOR " + unique_id}, status=401)
        else:
            document_sql.content = codecs.open(path_to_doc, 'r').read()
            document_sql.save()
            completed_work: [str] = [
                document_sql.unique_id,
                path_to_doc,
                'Database copy updated from filesystem.',
            ]
            return Response({"completed_work": completed_work})
    else:
        if not os.path.exists(os.path.join('static', 'web', 'krogoth_static_interface', doc_kind_formated)):
            os.makedirs(os.path.join("static", 'web', 'krogoth_static_interface', doc_kind_formated))
        doc_db_ref = KPubStaticInterfaceText(
            unique_id=unique_id,
            file_kind=doc_kind_formated,
            file_name=name_path,
            content=codecs.open(path_to_doc, 'r').read(),
            pub_date=datetime.now()
        )
        doc_db_ref.save()
        return Response({"brand new SQL record made": path_to_doc})


from django.urls import path

urlpatterns = [
    path('admin_editor_text/<str:name>/', AdminEditorText.as_view(), name="POST Create New Text Document"),
    path('admin_editor_text/', AdminEditorTextDetail.as_view(), name="PATCH Create New Text Document"),
    path('load_static_text_readonly/<str:filename>/', load_static_text_readonly, name="load_static_text_readonly"),
    path('get_uncommitted_docs/', get_uncommitted_docs, name="get_uncommitted_docs"),
    path('save_sqldb_to_filesystem_text/<str:file_name>/', save_sqldb_to_filesystem_text, name="Save SQL And Store Into HDD"),
    path('save_filesystem_to_sqldb_text/<str:file_name>/', save_filesystem_to_sqldb_text, name="Save HDD And Store Into SQL"),
    path('saveall_filesystem_to_sqldb_text/', saveall_filesystem_to_sqldb_text, name="Save HDD And Store Into SQL"),
]


"""
curl --location --request POST 'http://localhost:8000/global_static_text/admin_editor_text/' \
--form 'doc_name="FirstJavaScriptDoc2"' \
--form 'content="console.log(\"hello world\");"' \
--form 'doc_kind="js"'

curl --location --request PATCH 'http://localhost:8000/global_static_text/admin_editor_text/toolbar.controller.js/' \
--form 'doc_name="FirstJavaScriptDoc"' \
--form 'content="console.log(\"Hello world!\");\\n// COOL ITS GOOD. "'

curl --location --request GET 'http://localhost:8000/global_static_text/admin_editor_text/html/FirstJavaScriptDoc2' \
--form 'doc_name="HELLO6"' \
--form 'content="this is just a test"' \
--form 'doc_kind="html"'

curl --location --request GET 'http://localhost:8000/global_static_text/get_uncommitted_docs' \
--form 'doc_name="HELLO6"' \
--form 'content="this is just a test"' \
--form 'doc_kind="html"'

curl --location --request GET 'http://localhost:8000/global_static_text/save_sqldb_to_filesystem_text/toolbar.controller.js'

curl --location --request GET 'http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/toolbar.controller.js'

curl --location --request GET 'http://localhost:8000/global_static_text/saveall_filesystem_to_sqldb_text'

"""

















