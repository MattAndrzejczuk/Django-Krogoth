from LazarusDatabase.models import TotalAnnihilationMod
from rest_framework import serializers, exceptions




class TotalAnnihilationModSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalAnnihilationMod
        fields = '__all__'
