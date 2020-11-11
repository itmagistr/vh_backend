from rest_framework import serializers
import uuid
# import collections



class InvoiceInSerializer(serializers.Serializer):
	# https://developer.rbk.money/api/#operation/createInvoice
	# txt = serializers.CharField(max_length=50, allow_blank=True)
	# dt_start = serializers.DateTimeField(allow_null=True)
	# client_uid = serializers.CharField(max_length=36, allow_blank=True)
	medproc_uid = serializers.CharField(max_length=36, allow_blank=True)
	# doctor_uid = serializers.CharField(max_length=36, allow_blank=True)
	
	# def validate_client_uid(self, value):
	# 	if value is not None:
	# 		try:
	# 			uuid.UUID(value)
	# 		except:
	# 			raise serializers.ValidationError('This field must be uuid.')
	# 	return value

	def validate_medproc_uid(self, value):
		if value is not None:
			try:
				uuid.UUID(value)
			except:
				raise serializers.ValidationError('This field must be uuid.')
		return value

	# def validate_doctor_uid(self, value):
	# 	if value is not None:
	# 		try:
	# 			uuid.UUID(value)
	# 		except:
	# 			raise serializers.ValidationError('This field must be uuid.')
	# 	return value
	
	# def get_fields(self):
	# 	new_fields = collections.OrderedDict()
	# 	for name, field in super().get_fields().items():
	# 		field.required = False
	# 		new_fields[name] = field
	# 	return new_fields


class InvoiceOutSerializer(serializers.Serializer):
	invoice_id = serializers.CharField(max_length=20, allow_blank=False)
	invoice_expire = serializers.DateTimeField()
	invoice_token = serializers.CharField(max_length=255, allow_blank=False)
	invoice_status = serializers.CharField(max_length=20, allow_blank=False)
	invoice_title = serializers.CharField(max_length=35, allow_blank=False)
	invoice_email = serializers.CharField(max_length=35, allow_blank=False)
	invoice_desc = serializers.CharField(max_length=255, allow_blank=False)

class InvoiceOutErrorSerializer(serializers.Serializer):
	response_code = serializers.IntegerField()
	message = serializers.CharField(max_length=255, allow_blank=True)
