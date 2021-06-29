from .models import *
from rest_framework import serializers
from vh_human.serializers import HumanSerializer
import uuid
import collections


class SpecialRuSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_ru')
	class Meta:
		model = Special
		fields = [ 'title', 'img']

class SpecialCodeEnSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_en')
	class Meta:
		model = Special
		fields = [ 'code', 'title', 'img']

class SpecialCodeRuSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_ru')
	class Meta:
		model = Special
		fields = [ 'code', 'title', 'img']

class SpecialCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Special
		fields = ['code']

class DoctorWorkResSerializer(serializers.ModelSerializer):#serializers.HyperlinkedModelSerializer):
	doc_uid = serializers.CharField(source='doctor.uid')
	class Meta:
		model = DocWorkRes
		fields = ['doc_uid', 'pos', 'img', 'title']

class DoctorRuSerializer(serializers.ModelSerializer):#serializers.HyperlinkedModelSerializer):
	lastName = serializers.CharField(source='lastName_ru')
	firstName = serializers.CharField(source='firstName_ru')
	special = serializers.CharField(default='...', source='special.title_ru')
	special_img = serializers.ImageField(source='special.img')
	midName = serializers.CharField(default='', source='midName_ru')
	img = serializers.ImageField(source='image', default='media/doctors/doc1.png')
	experience = serializers.IntegerField(default=1)
	degree = serializers.CharField(default='...', source='degree.title_ru')
	level = serializers.CharField(default='...', source='level.title_ru')
	rating = serializers.DecimalField(default=4, max_digits=5, decimal_places=1, source='rating.rate')
	reviewCount = serializers.IntegerField(default=0)
	сertificate = serializers.CharField(default='...', source='сertificate_ru')
	education = serializers.CharField(default='...', source='education_ru')
	class Meta:
		model = Doctor
		fields = ['uid', 'lastName', 'firstName', 'special', 'special_img', 'midName', 'img', 'experience', 'degree', 'level', 'rating', 'reviewCount', 'youtube', 'fb', 'vk', 'insta', 'сertificate', 'education']

class DoctorEnSerializer(serializers.ModelSerializer):#serializers.HyperlinkedModelSerializer):
	lastName = serializers.CharField(source='lastName_en')
	firstName = serializers.CharField(source='firstName_en')
	special = serializers.CharField(source='special.title_en')
	special_img = serializers.ImageField(source='special.img')
	midName = serializers.CharField(default='', source='midName_en')
	img = serializers.ImageField(source='image', default='media/doctors/doc1.png')
	experience = serializers.IntegerField(default=1)
	degree = serializers.CharField(default='...', source='degree.title_en')
	level = serializers.CharField(default='...', source='level.title_en')
	rating = serializers.DecimalField(default=4, max_digits=5, decimal_places=1, source='rating.rate')
	reviewCount = serializers.IntegerField(default=0)
	сertificate = serializers.CharField(default='...', source='сertificate_en')
	education = serializers.CharField(default='...', source='education_en')

	class Meta:
		model = Doctor
		fields = ['uid', 'lastName', 'firstName', 'special', 'special_img', 'midName', 'img', 'experience', 'degree', 'level', 'rating', 'reviewCount', 'youtube', 'fb', 'vk', 'insta', 'сertificate', 'education']

class DoctorFilterSerializer(serializers.Serializer):
	txt = serializers.CharField(max_length=50, allow_blank=True)
	dt = serializers.DateField(allow_null=True)
	medproc_uid = serializers.CharField(max_length=36, allow_blank=True)
	spec = SpecialCodeSerializer(many=True)
	
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

class DoctorLightRuSerializer(serializers.ModelSerializer):
	lastName = serializers.CharField(source='lastName_ru')
	firstName = serializers.CharField(source='firstName_ru')
	special = serializers.CharField(source='special.title_ru')
	special_img = serializers.ImageField(source='special.img')
	midName = serializers.CharField(default='', source='midName_ru')
	img = serializers.ImageField(source='image', default='media/doctors/doc1.png')
	experience = serializers.IntegerField(default=1)
	level = serializers.CharField(default='...', source='level.title_ru')
	rating = serializers.DecimalField(default=4, max_digits=5, decimal_places=1, source='rating.rate')
	reviewCount = serializers.IntegerField(default=0)
	class Meta:
		model = Doctor
		fields = ['uid', 'lastName', 'firstName', 'special', 'special_img', 'midName', 'img', 'experience', 'level', 'rating', 'reviewCount']

class DoctorLightEnSerializer(serializers.ModelSerializer):#serializers.HyperlinkedModelSerializer):
	lastName = serializers.CharField(source='lastName_en')
	firstName = serializers.CharField(source='firstName_en')
	special = serializers.CharField(source='special.title_en')
	special_img = serializers.ImageField(source='special.img')
	midName = serializers.CharField(default='', source='midName_en')
	img = serializers.ImageField(source='image', default='media/doctors/doc1.png')
	experience = serializers.IntegerField(default=1)
	level = serializers.CharField(default='...', source='level.title_en')
	rating = serializers.DecimalField(default=4, max_digits=5, decimal_places=1, source='rating.rate')
	reviewCount = serializers.IntegerField(default=0)
	class Meta:
		model = Doctor
		fields = ['uid', 'lastName', 'firstName', 'special', 'special_img', 'midName', 'img', 'experience', 'level', 'rating', 'reviewCount']