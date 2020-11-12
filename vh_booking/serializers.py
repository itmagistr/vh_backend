from .models import Booking
from rest_framework import serializers
from vh_medproc.serializers import *
import uuid
import collections



class BookingReadSerializer(serializers.ModelSerializer):
	#medproc = serializers.SlugRelatedField(read_only=True, slug_field='title')
	medproc = MedProcRuSerializer(read_only=True)
	client = serializers.SlugRelatedField(read_only=True, slug_field='human_fio')
	doctor = serializers.SlugRelatedField(read_only=True, slug_field='human_fio')
	class Meta:
		model = Booking
		fields = ['uid', 'dt_start', 'dt_expire', 'status', 'medproc', 'doctor', 'client',]




class BookingFilterSerializer(serializers.Serializer):
	txt = serializers.CharField(max_length=50, allow_blank=True)
	dt_start = serializers.DateTimeField(allow_null=True)
	client_uid = serializers.CharField(max_length=36, allow_blank=True)
	medproc_uid = serializers.CharField(max_length=36, allow_blank=True)
	doctor_uid = serializers.CharField(max_length=36, allow_blank=True)
	
	def validate_client_uid(self, value):
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


class BookingCreateSerializer(serializers.Serializer):
	dt_start = serializers.DateTimeField(allow_null=False)
	medproc_uid = serializers.CharField(max_length=36, allow_blank=False)
	doctor_uid = serializers.CharField(max_length=36, allow_blank=True)
	client_uid = serializers.CharField(max_length=36, allow_blank=True)
	comment = serializers.CharField(max_length=50, allow_blank=True)