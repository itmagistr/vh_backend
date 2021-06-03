from .models import MedProc
from rest_framework import serializers
import uuid
import collections
#from vh_product.serializers import *

class MedProcEnSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_en')
	title_check = serializers.CharField(source='title_check_en')
	description = serializers.CharField(source='description_en')
	recomend_before = serializers.CharField(source='recomend_before_en')
	recomend_after = serializers.CharField(source='recomend_after_en')
	# uid = serializers.CharField(source='product.uid')
	# title = serializers.CharField(source='product.title')
	# title_check = serializers.CharField(source='product.title_check')
	# price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)
	# price_old = serializers.DecimalField(source='product.price_old', max_digits=10, decimal_places=2)
	# description = serializers.CharField(source='product.description')
	# #product = ProductSerializer()
	class Meta:
		model = MedProc
		fields = ['uid', 'code', 'title', 'title_check', 'description', 'price', 'price_old', 'duration', 'recomend_before', 'recomend_after']

class MedProcRuSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_ru')
	title_check = serializers.CharField(source='title_check_ru')
	description = serializers.CharField(source='description_ru')
	recomend_before = serializers.CharField(source='recomend_before_ru')
	recomend_after = serializers.CharField(source='recomend_after_ru')
	class Meta:
		model = MedProc
		fields = ['uid', 'code', 'title', 'title_check', 'description', 'price', 'price_old', 'duration', 'recomend_before', 'recomend_after']


class MedProcFilterSerializer1(serializers.Serializer):
	mp_code = serializers.CharField(max_length=20, allow_blank=True)
	mp_title = serializers.CharField(max_length=50, allow_blank=True)

def is_uuid(value):
	try:
		uuid.UUID(value)
	except:
		raise serializers.ValidationError('This field must be uuid.')

class MedProcFilterSerializer(serializers.Serializer):
	txt = serializers.CharField(max_length=50, allow_blank=True)
	dt = serializers.DateField(allow_null=True)
	doctor_uid = serializers.CharField(max_length=36, allow_blank=True)
	
	def validate_doctor_uid(self, value):
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

class MedProcSearchSerializer(serializers.Serializer):
	q = serializers.CharField(max_length=50, allow_blank=True)
	
	