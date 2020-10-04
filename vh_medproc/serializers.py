from .models import MedProc
from rest_framework import serializers


class MedProcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedProc
        fields = ['uid', 'title', 'description', 'duration']

