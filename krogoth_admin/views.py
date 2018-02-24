from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from krogoth_admin.serializers import UncommitedSQLSerializer
from krogoth_admin.models import UncommitedSQL


class UncommitedSQLViewSet(viewsets.ModelViewSet):
    queryset = UncommitedSQL.objects.all()
    serializer_class = UncommitedSQLSerializer
    permission_classes = (IsAdminUser,)

