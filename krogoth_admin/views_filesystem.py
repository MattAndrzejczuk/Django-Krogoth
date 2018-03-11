from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser
from krogoth_gantry.models import KrogothGantryService
from jawn.settings import BASE_DIR
import os

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
