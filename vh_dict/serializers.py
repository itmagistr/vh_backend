from .models import DictString
from rest_framework import serializers

import collections


class DictStrRuSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_ru')
	title_short = serializers.CharField(source='title_short_ru')
	class Meta:
		model = DictString
		fields = ['code', 'title', 'title_short', ]

class DictStrEnSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_en')
	title_short = serializers.CharField(source='title_short_en')
	class Meta:
		model = DictString
		fields = ['code', 'title', 'title_short', ]

class DictStrFilterSerializer(serializers.Serializer):
	code = serializers.CharField(max_length=20, allow_blank=False)
                	
	def get_fields(self):
		new_fields = collections.OrderedDict()
		for name, field in super().get_fields().items():
			field.required = False
			new_fields[name] = field
		return new_fields
