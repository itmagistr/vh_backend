from .models import Feedback, FeedbackType
from rest_framework import serializers
import collections
#

class FeedBackSerializer(serializers.ModelSerializer):
	fb_type = serializers.CharField(source='fb_type.code')
	class Meta:
		model = Feedback
		fields = ['uid', 'fb_type', 'name', 'phone', 'email', 'call_hr', 'call_mn', 'message']


class FBCreateSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=50, allow_blank=False)
	phone = serializers.RegexField(regex='\d+', allow_blank=False)
	email = serializers.EmailField(allow_blank=False)
	message = serializers.CharField(allow_blank=False)
	recap = serializers.CharField(max_length=255, allow_blank=True)


class FBCallCreateSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=50, allow_blank=False)
	phone = serializers.RegexField(regex='\d{11,16}', allow_blank=False)
	hr = serializers.IntegerField(min_value=6, max_value=23)
	min = serializers.IntegerField(min_value=0, max_value=59)
	recap = serializers.CharField(max_length=255, allow_blank=True)

	def get_fields(self):
		new_fields = collections.OrderedDict()
		for name, field in super().get_fields().items():
			field.required = False
			new_fields[name] = field
		return new_fields