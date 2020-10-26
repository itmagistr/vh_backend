from .models import Doctor, Special
from rest_framework import serializers
from vh_human.serializers import HumanSerializer



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

