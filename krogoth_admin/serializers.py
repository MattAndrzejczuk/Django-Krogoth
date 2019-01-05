from rest_framework import serializers
from krogoth_admin.models import UncommitedSQL
from chat.serializers import JawnUserSerializer

class UncommitedSQLSerializer(serializers.ModelSerializer):
    edited_by = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = UncommitedSQL
        fields = '__all__'