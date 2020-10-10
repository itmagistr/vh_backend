from django.contrib.auth.models import User, Group
from rest_framework import serializers


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