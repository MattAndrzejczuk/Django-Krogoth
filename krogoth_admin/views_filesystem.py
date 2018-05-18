from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser
from krogoth_gantry.models import KrogothGantryService, KrogothGantryCategory, KrogothGantryIcon, \
    KrogothGantryMasterViewController, KrogothGantryDirective, AKGantryMasterViewController
from moho_extractor.models import IncludedHtmlMaster
from jawn.settings import BASE_DIR
import json
import os



# Generate New MVC
class CreateNewMVCView(APIView):

    def create_directory(self, named: str):
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/" + named
        print(sys_path)
        if (os.path.isdir(sys_path)):
            pass
        else:
            os.makedirs(sys_path)

    def create_subdirectory(self, named: str, within: str):
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/" + within + "/" + named
        print(sys_path)
        if (os.path.isdir(sys_path)):
            pass
        else:
            os.makedirs(sys_path)
        pass

    def create_master_file(self, named: str, ext: str, with_contents: str, category: str, subcategory: str, kind: str) -> str:
        p1 = BASE_DIR + "/krogoth_gantry/DVCManager/" + category + "/" + subcategory
        sys_path = p1 + "/" + named + "/MasterVC/" + kind + "." + ext
        print(sys_path)
        if not os.path.exists(p1 + "/" + named + "/MasterVC/"):
            os.makedirs(p1 + "/" + named + "/")
            os.makedirs(p1 + "/" + named + "/MasterVC/")
            f = open(p1 + "/" + named + "/Title.txt", "w+")
            f.write(named.replace("_", " "))
            f.close()
        #os.mknod(sys_path)
        f = open(sys_path, "w+")
        f.write(with_contents)
        f.close()
        return p1 + "/" + named + "/"

    def create_subcat_json_file(self, json_dump: str, category: str, subcategory: str):
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/" + category + "/" + subcategory + "/subcat.json"
        print(sys_path)
        f = open(sys_path, "w+")
        f.write(json_dump)
        f.close()

    def create_cat_json_file(self, json_dump: str, category: str):
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/" + category + "/category.json"
        print(sys_path)
        f = open(sys_path, "w+")
        f.write(json_dump)
        f.close()

    def post(self, request, format=None):
        name = str(request.data["name"])
        cat_ = str(request.data["cat"])
        subcat = str(request.data["subcat"])
        weight = int(request.data["weight"])
        app_icon = str(request.data["app_icon"])
        app_icon_prefix = str(request.data["app_icon_prefix"])
        cat_icon = str(request.data["cat_icon"])
        cat_icon_prefix = str(request.data["cat_icon_prefix"])
        subcat_icon = str(request.data["subcat_icon"])
        subcat_icon_prefix = str(request.data["subcat_icon_prefix"])
        is_lazy = bool(int(request.data["is_lazy"]))

        cat_json = json.dumps({
            "icon": cat_icon,
            "prefix": cat_icon_prefix,
            "weight": weight
        }, indent=2, sort_keys=True)
        subcat_json = json.dumps({
            "icon": subcat_icon,
            "prefix": subcat_icon_prefix,
            "weight": weight
        }, indent=2, sort_keys=True)

        app_obj = AKGantryMasterViewController()
        mvc_already_exists = bool(len(AKGantryMasterViewController.objects.filter(name=name)))
        if mvc_already_exists:
            return Response({"result": "mvc with that name already exists."}, status=405)

        app_obj = AKGantryMasterViewController(name=name, title=name.replace("_", " "))

        cat_exists = bool(len(KrogothGantryCategory.objects.filter(name=cat_)))
        subcat_exists = bool(len(KrogothGantryCategory.objects.filter(name=subcat)))

        cat_obj = KrogothGantryCategory()
        subcat_obj = KrogothGantryCategory()

        self.create_directory(named=cat_)
        self.create_subdirectory(named=subcat, within=cat_)

        if cat_exists:
            cat_obj = KrogothGantryCategory.objects.get(name=cat_)
        else:
            cat_obj = KrogothGantryCategory(name=cat_, title=cat_.replace("_", " "))
            cat_icon_exists = bool(len(KrogothGantryIcon.objects.filter(code=cat_icon)))
            if cat_icon_exists:
                cat_obj.icon = KrogothGantryIcon.objects.get(code=cat_icon)
            else:
                ico = KrogothGantryIcon(code=cat_icon, prefix=cat_icon_prefix)
                ico.save()
                cat_obj.icon = ico
            cat_obj.save()
            self.create_cat_json_file(json_dump=cat_json, category=cat_)

        if subcat_exists:
            subcat_obj = KrogothGantryCategory.objects.get(name=subcat)
        else:
            subcat_obj = KrogothGantryCategory(name=subcat, title=subcat.replace("_", " "))
            subcat_icon_exists = bool(len(KrogothGantryIcon.objects.filter(code=subcat_icon)))
            if subcat_icon_exists:
                subcat_obj.icon = KrogothGantryIcon.objects.get(code=subcat_icon)
            else:
                ico = KrogothGantryIcon(code=subcat_icon, prefix=subcat_icon_prefix)
                ico.save()
                subcat_obj.icon = ico
            subcat_obj.parent = cat_obj
            subcat_obj.save()
            self.create_subcat_json_file(json_dump=subcat_json, category=cat_, subcategory=subcat)

        app_icon_exists = bool(len(KrogothGantryIcon.objects.filter(code=app_icon)))
        if app_icon_exists:
            app_obj.icon = KrogothGantryIcon.objects.get(code=app_icon)
        else:
            ico = KrogothGantryIcon(code=app_icon, prefix=app_icon_prefix)
            ico.save()
            app_obj.icon = ico

        app_obj.category = subcat_obj
        app_obj.is_lazy = is_lazy

        root_mvc_path = self.create_master_file(named=name,ext="html",with_contents=app_obj.view_html,category=cat_, subcategory=subcat,kind="view")
        self.create_master_file(named=name, ext="js", with_contents=app_obj.module_js, category=cat_,
                                subcategory=subcat, kind="module")
        self.create_master_file(named=name, ext="js", with_contents=app_obj.controller_js, category=cat_,
                                subcategory=subcat, kind="controller")
        self.create_master_file(named=name, ext="css", with_contents=app_obj.style_css, category=cat_,
                                subcategory=subcat, kind="style")
        self.create_master_file(named=name, ext="css", with_contents=app_obj.themestyle, category=cat_,
                                subcategory=subcat, kind="themestyle")
        print("\n")
        print(root_mvc_path)
        app_obj.path_to_static = root_mvc_path
        app_obj.save()

        return Response({"result": "success"}, status=201)

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
        print("\n\nOLD: " + old_path)
        print("\n\nNEW: " + new_path)
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
        print("\n\nOLD: " + old_path)
        print("\n\nNEW: " + new_path)
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
        old_name = ""
        try:
            old_name = str(request.data["old_name"]).split("?name=")[1]
        except:
            old_name = str(request.data["old_name"])
        old_name = str(request.data["old_name"]).split("?name=")[1]
        new_name = str(request.data["new_name"])
        sys_path = BASE_DIR + "/krogoth_gantry/DVCManager/"
        sql_path = path_0 + "/" + path_1 + "/" + path_2 + "/partialsHTML/"
        old_path = sys_path + sql_path + old_name + ".html"
        new_path = sys_path + sql_path + new_name + ".html"
        print("\n\nOLD: " + old_path)
        print("\n\nNEW: " + new_path)
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


