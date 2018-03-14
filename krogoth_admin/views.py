from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from krogoth_admin.serializers import UncommitedSQLSerializer
from krogoth_admin.models import UncommitedSQL
from rest_framework.views import APIView
from rest_framework.response import Response
import os


class UncommitedSQLViewSet(viewsets.ModelViewSet):
    queryset = UncommitedSQL.objects.all()
    serializer_class = UncommitedSQLSerializer
    permission_classes = (IsAdminUser,)


# Services
class SaveSQLToFileSystemView(APIView):

    def get(self, request, format=None):
        os.system("./manage.py backupdvc")
        return Response({"result": "success"}, status=200)