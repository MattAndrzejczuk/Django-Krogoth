# coding=utf-8
__version__ = '0.9.53'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers
from kbot_lab.models import KBNanolatheExampleUpload, KBNanolatheAbstractBlueprint, KBNanolatheExamplePlain


class KBNanolatheAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = KBNanolatheAbstractBlueprint
        fields = ('html_code',)

    html_code = serializers.SerializerMethodField()

    def get_html_code(self, obj):
        return '<div>no code generation yet.</div>'





class KBNanolatheExampleUploadSerializer(KBNanolatheAbstractSerializer):
    class Meta:
        model = KBNanolatheExampleUpload
        fields = KBNanolatheAbstractSerializer.Meta.fields + ('kb_file','kbc_uploaded_by_user',)

    kb_file = serializers.FileField()
    # modified = serializers.HiddenField(default=timezone.now)


    # def create(self, validated_data):
    #     # if validated_data['kbc_uploaded_by_user'] is None:
    #     #     jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
    #     #     new_upload.kbc_uploaded_by_user = jawn_user
    #     return validated_data

class KBNanolatheExamplePlainSerializer(KBNanolatheAbstractSerializer):
    class Meta:
        model = KBNanolatheExamplePlain
        fields = KBNanolatheAbstractSerializer.Meta.fields + ('title','num_value',)

