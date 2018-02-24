from rest_framework import serializers
from krogoth_admin.models import UncommitedSQL


class UncommitedSQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = UncommitedSQL
        fields = '__all__'