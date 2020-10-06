from .models import Doctor, Special
from rest_framework import serializers

class SpecialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Special
		fields = ['uid', 'title']


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
	special = SpecialSerializer()
	class Meta:
		model = Doctor
		fields = ['uid', 'lastName', 'firstName', 'title', 'phone', 'special']

