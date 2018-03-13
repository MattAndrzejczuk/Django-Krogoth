from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser
from krogoth_gantry.models import KrogothGantryService, KrogothGantryMasterViewController, KrogothGantryDirective
from moho_extractor.models import IncludedHtmlMaster
from jawn.settings import BASE_DIR
import os


# Services
class RenameService(APIView):
    #permission_classes = (IsAdminUser)
    def post(self, request, format=None):
        path_0 = str(request.data["path_0"])
        path_1 = str(request.data["path_1"])
        path_2 = str(request.data["path_2"])

        old_name = str(request.data["old_name"])
        new_name = str(request.data["new_name"])

        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
        sql_path = path_0 + "/" + path_1 + "/" + path_2 + "/Services/"

        old_path = sys_path + sql_path + old_name + ".js"
        new_path = sys_path + sql_path + new_name + ".js"

        os.rename(old_path, new_path)
        renamed_sql = KrogothGantryService.objects.get(name=old_name)
        renamed_sql.name = new_name
        renamed_sql.title = new_name
        renamed_sql.save()
        return Response({"result": "success"}, status=200)

class CreateService(APIView):
    def post(self, request, format=None):
        path_0 = str(request.data["path_0"])
        path_1 = str(request.data["path_1"])
        index = int(request.data["index"])
        master_name = str(request.data["master_name"])
        new_name = str(request.data["new_name"])
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
        sql_path = path_0 + "/" + path_1 + "/" + master_name + "/Services/"
        if not os.path.isdir(sys_path + sql_path):
            os.makedirs(sys_path + sql_path)
        new_path = sys_path + sql_path + new_name + ".js"
        make_blank = open(new_path, 'w')
        make_blank.write("/* " + new_name + " Service */")
        make_blank.close()
        new_sql = KrogothGantryService(name=new_name, title=new_name)
        new_sql.save()
        mastervc = KrogothGantryMasterViewController.objects.get(name=master_name)
        mastervc.djangular_service.add(new_sql)
        mastervc.save()
        node_for_frontend = {
            "id": new_sql.id,
            "parentIndex": 4,
            "index": index,
            "name": new_sql.name,
            "title": new_sql.title,
            "class": "Service",
            "nodes": 0,
            "canRemove": True,
            "canEdit": True,
            "isMaster": False,
            "sourceCode": new_sql.service_js,
            "sourceKey": "service_js",
            "RESTfulId": new_sql.id,
            "RESTfulURI": "/krogoth_gantry/viewsets/Service/" + str(new_sql.id) + "/",
            "syntax": "javascript",
            "hasUnsavedChanges": False,
            "icon": "language-javascript"
        }
        return Response(node_for_frontend, status=201)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Directives
class RenameDirective(APIView):
    # permission_classes = (IsAdminUser)
    def post(self, request, format=None):
        path_0 = str(request.data["path_0"])
        path_1 = str(request.data["path_1"])
        path_2 = str(request.data["path_2"])
        old_name = str(request.data["old_name"])
        new_name = str(request.data["new_name"])
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
        sql_path = path_0 + "/" + path_1 + "/" + path_2 + "/Directives/"
        old_path = sys_path + sql_path + old_name + ".js"
        new_path = sys_path + sql_path + new_name + ".js"
        os.rename(old_path, new_path)
        renamed_sql = KrogothGantryDirective.objects.get(name=old_name)
        renamed_sql.name = new_name
        renamed_sql.title = new_name
        renamed_sql.save()
        return Response({"result": "success"}, status=200)

class CreateDirective(APIView):
    # permission_classes = (IsAdminUser)
    def post(self, request, format=None):
        path_0 = str(request.data["path_0"])
        path_1 = str(request.data["path_1"])
        index = int(request.data["index"])
        master_name = str(request.data["master_name"])
        new_name = str(request.data["new_name"])
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
        sql_path = path_0 + "/" + path_1 + "/" + master_name + "/Directives/"
        if not os.path.isdir(sys_path + sql_path):
            os.makedirs(sys_path + sql_path)
        new_path = sys_path + sql_path + new_name + ".js"
        make_blank = open(new_path, 'w')
        make_blank.write("/* " + new_name + " Directive */")
        make_blank.close()
        new_sql = KrogothGantryDirective(name=new_name, title=new_name)
        new_sql.save()
        mastervc = KrogothGantryMasterViewController.objects.get(name=master_name)
        mastervc.djangular_directive.add(new_sql)
        mastervc.save()
        node_for_frontend = {
            "id": new_sql.id,
            "parentIndex": 3,
            "index": index,
            "name": new_sql.name,
            "title": new_sql.title,
            "class": "Directive",
            "nodes": 0,
            "canRemove": True,
            "canEdit": True,
            "isMaster": False,
            "sourceCode": new_sql.directive_js,
            "sourceKey": "directive_js",
            "RESTfulId": new_sql.id,
            "RESTfulURI": "/krogoth_gantry/viewsets/Directive/" + str(new_sql.id) + "/",
            "syntax": "javascript",
            "hasUnsavedChanges": False,
            "icon": "language-javascript"
        }
        return Response(node_for_frontend, status=201)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Templates
class RenameTemplate(APIView):
    # permission_classes = (IsAdminUser)
    def post(self, request, format=None):
        path_0 = str(request.data["path_0"])
        path_1 = str(request.data["path_1"])
        path_2 = str(request.data["path_2"])
        old_name = str(request.data["old_name"])
        new_name = str(request.data["new_name"])
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
        sql_path = path_0 + "/" + path_1 + "/" + path_2 + "/partialsHTML/"
        old_path = sys_path + sql_path + old_name + ".html"
        new_path = sys_path + sql_path + new_name + ".html"
        os.rename(old_path, new_path)
        renamed_sql = IncludedHtmlMaster.objects.get(name=old_name)
        renamed_sql.name = new_name
        renamed_sql.title = new_name
        renamed_sql.save()
        return Response({"result": "success"}, status=200)

class CreateTemplate(APIView):
    def post(self, request, format=None):
        path_0 = str(request.data["path_0"])
        path_1 = str(request.data["path_1"])
        index = int(request.data["index"])
        master_name = str(request.data["master_name"])
        new_name = str(request.data["new_name"])
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
        sql_path = path_0 + "/" + path_1 + "/" + master_name + "/partialsHTML/"
        if not os.path.isdir(sys_path + sql_path):
            os.makedirs(sys_path + sql_path)
        new_path = sys_path + sql_path + new_name + ".html"
        new_sql = IncludedHtmlMaster(name=new_name)

        make_blank = open(new_path, 'w')
        make_blank.write("/* " + new_name + " IncludedHtmlMaster */\n\n" + new_sql.contents)
        make_blank.close()
        mastervc = KrogothGantryMasterViewController.objects.get(name=master_name)
        # mastervc.partial_html.add(new_sql)
        # mastervc.save()
        new_sql.master_vc = mastervc
        new_sql.save()
        node_for_frontend = {
            "id": new_sql.id,
            "parentIndex": 5,
            "index": index,
            "name": new_sql.name,
            "title": new_sql.name,
            "class": "NgIncludedHtml",
            "nodes": 0,
            "canRemove": True,
            "canEdit": True,
            "isMaster": False,
            "sourceCode": new_sql.contents,
            "sourceKey": "contents",
            "RESTfulId": new_sql.id,
            "RESTfulURI": "/krogoth_gantry/viewsets/IncludedHtmlMaster/" + str(new_sql.id) + "/",
            "syntax": "htmlmixed",
            "hasUnsavedChanges": False,
            "icon": "link-variant"
        }
        return Response(node_for_frontend, status=201)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


