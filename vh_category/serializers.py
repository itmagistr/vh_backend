from .models import Category
from rest_framework import serializers

import uuid
import collections


class CategoryRuSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_ru')
	title_short = serializers.CharField(source='title_short_ru')
	description = serializers.CharField(source='description_ru')
	class Meta:
		model = Category
		fields = [ 'code', 'title', 'title_short', 'img', 'description']

class CategoryEnSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='title_en')
	title_short = serializers.CharField(source='title_short_en')
	description = serializers.CharField(source='description_en')
	class Meta:
		model = Category
		fields = [ 'code', 'title', 'title_short', 'img', 'description']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = [ 'code']
