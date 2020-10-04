from .models import Doctor
from rest_framework import serializers


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['uid', 'lastName', 'firstName', 'title', 'phone', 'special', 'usr']

