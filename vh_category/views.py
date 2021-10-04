from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.utils import translation
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging
logger = logging.getLogger(__name__)
# Create your views here.

class CategoryListView(generics.ListAPIView):
	'''
	Получить Категории группировки мед процедур
	'''
	serializer_class = CategoryEnSerializer
	# lookup_field = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return CategoryRuSerializer
		return CategoryEnSerializer
		
	def get_queryset(self):
		mp = Category.objects.filter(code__exact='MEDPROCS')
		return Category.objects.filter(parent=mp[0])

class CategoryItemView(generics.RetrieveAPIView):
	'''
	Получить категорию по code.
	'''
	serializer_class = CategoryEnSerializer
	lookup_field = 'code'
	def get_serializer_class(self):
		if 'ru' in translation.get_language():
			return CategoryRuSerializer
		return CategoryEnSerializer
		
	def get_queryset(self):
		return Category.objects.all()
