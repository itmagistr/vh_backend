from .models import Doctor, Special
from rest_framework import serializers
from vh_human.serializers import HumanSerializer
import uuid
import collections


class SpecialRuSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_ru')
	class Meta:
		model = Special
		fields = [ 'title']


class DoctorRuSerializer(serializers.ModelSerializer):#serializers.HyperlinkedModelSerializer):
	lastName = serializers.CharField(source='lastName_ru')
	firstName = serializers.CharField(source='firstName_ru')
	special = serializers.CharField(source='special.title_ru')

	#special = SpecialRuSerializer()
	class Meta:
		model = Doctor
		fields = ['uid', 'lastName', 'firstName', 'special']

class DoctorEnSerializer(serializers.ModelSerializer):#serializers.HyperlinkedModelSerializer):
	lastName = serializers.CharField(source='lastName_en')
	firstName = serializers.CharField(source='firstName_en')
	special = serializers.CharField(source='special.title_en')

	#special = SpecialRuSerializer()
	class Meta:
		model = Doctor
		fields = ['uid', 'lastName', 'firstName', 'special']

class DoctorFilterSerializer(serializers.Serializer):
	txt = serializers.CharField(max_length=50, allow_blank=True)
	dt = serializers.DateField(allow_null=True)
	medproc_uid = serializers.CharField(max_length=36, allow_blank=True)
	
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