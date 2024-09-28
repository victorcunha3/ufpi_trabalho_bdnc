from rest_framework import serializers
from .models import Patient
import json

class PatientSerializer(serializers.ModelSerializer):
    #sintomas = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Patient
        fields = '__all__'