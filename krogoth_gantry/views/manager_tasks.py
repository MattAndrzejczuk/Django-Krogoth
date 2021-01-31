from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from krogoth_gantry.functions.uncommited_SQL import UncommitedSQLSerializer
from krogoth_gantry.models.krogoth_manager import UncommitedSQL
from rest_framework.views import APIView
from rest_framework.response import Response
import os

from krogoth_gantry.models.gantry_models import KrogothGantryMasterViewController
from krogoth_gantry.krogoth_compiler import MasterCompiler

class UncommitedSQLViewSet(viewsets.ModelViewSet):
    queryset = UncommitedSQL.objects.all()
    serializer_class = UncommitedSQLSerializer
    permission_classes = (IsAdminUser,)


# Services
class SaveSQLToFileSystemView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, format=None):
        os.system("./manage.py backupdvc")
        return Response({"result": "success"}, status=200)


class CollectStatic(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, format=None):
        os.system("./manage.py collectstatic --no-input")
        return Response({"result": "success"}, status=200)


class CompileMVCsToStatic(APIView):
    # permission_classes = (IsAdminUser, )
    def get(self, request, format=None):
        masters = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
        for master in masters:
            compiler = MasterCompiler(username="Guest")
            compiled_js = compiler.compiled_raw(named=master.name)
            text_file = open("static/compiled/"+master.name+".js", "w")
            text_file.write(compiled_js)
            text_file.close()
        os.system("./manage.py collectstatic --no-input")
        return Response({"result": "success"}, status=200)
