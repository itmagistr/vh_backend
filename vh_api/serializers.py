from django.contrib.auth.models import User, Group
from rest_framework import serializers
import uuid
import collections


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DayStatusSerializer(serializers.Serializer):
    d = serializers.CharField(max_length=20)
    s = serializers.IntegerField()

class TimeStatusSerializer(serializers.Serializer):
    t = serializers.CharField(max_length=5)
    s = serializers.IntegerField()

class DaySerializer(serializers.Serializer):
    dt = serializers.DateField()
    medproc_uid = serializers.CharField(max_length=36, allow_blank=True)
    doctor_uid = serializers.CharField(max_length=36, allow_blank=True)
    
    def validate_doctor_uid(self, value):
        if value is not None:
            try:
                uuid.UUID(value)
            except:
                raise serializers.ValidationError('This field must be uuid.')
        return value

    def validate_medproc_uid(self, value):
        if value is not None:
            try:
                uuid.UUID(value)
            except:
                raise serializers.ValidationError('This field must be uuid.')
        return value
    
    def get_fields(self):
        new_fields = collections.OrderedDict()
        for name, field in super().get_fields().items():
            field.required = False
            new_fields[name] = field
        return new_fields

class PeriodSerializer(serializers.Serializer):
    dstart = serializers.DateField()
    dend = serializers.DateField()

class LuckyDaySerializer(serializers.Serializer):
    dt = serializers.DateField()
