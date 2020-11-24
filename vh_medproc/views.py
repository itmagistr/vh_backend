from django.shortcuts import render
#from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.utils import translation
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import logging
logger = logging.getLogger(__name__)

# Create your views here.

# class MedProcViewSet(viewsets.ReadOnlyModelViewSet):
# 	'''
# 	Получить процедуру по умолчанию.
# 	'''
# 	serializer_class = MedProcEnSerializer
# 	http_method_names = ['get']
# 	def get_serializer_class(self):
# 		logger.info(translation.get_language())

# 		if 'ru' in translation.get_language():
# 			# using 'in' because it can be set to something like 'es-ES; es'
# 			return MedProcRuSerializer
# 		return MedProcEnSerializer
		
# 	def get_queryset(self):
# 		return MedProc.objects.all()


class MedProcListView(generics.RetrieveAPIView):
	'''
	Получить процедуру по умолчанию.
	'''
	serializer_class = MedProcEnSerializer
	#lookup_field = 'uid'
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer
		
	def get_queryset(self):
		return MedProc.objects.filter(code='B01.063.001')
	def get_object(self):
		obj = get_object_or_404(self.get_queryset())
		return obj


class MedProcView(generics.RetrieveAPIView):
	'''
	Получить процедуру по uid.
	'''
	serializer_class = MedProcEnSerializer
	lookup_field = 'uid'
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer
		
	def get_queryset(self):
		return MedProc.objects.all()


class MedProcFilterView1(generics.ListAPIView):
	'''
	depricated - Поиск процедур по части наименования или коду процедуры
	'''
	serializer_class = MedProcEnSerializer
	http_method_names = ['post']
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer
	@swagger_auto_schema(request_body=MedProcFilterSerializer1, responses={201: MedProcRuSerializer,}, deprecated=True)
	def post(self, request, *args, **kwargs):
		serializer = MedProcFilterSerializer1(data=request.data)
		serializer.is_valid(raise_exception=True)
		sclass = self.get_serializer_class()
		if 'Ru' in str(sclass):
			resSerializer = sclass(MedProc.objects.filter(Q(code__startswith=serializer.data['mp_code']) | Q(title_ru__icontains=serializer.data['mp_title']) ), many=True)
		else:
			resSerializer = sclass(MedProc.objects.filter(Q(code__startswith=serializer.data['mp_code']) | Q(title_en__icontains=serializer.data['mp_title']) ), many=True)
		#headers = self.get_success_headers(resSerializer.data)
		return Response(resSerializer.data, status=status.HTTP_200_OK) #, headers=resSerializer.headers


class MedProcFilterView(generics.ListAPIView):
	'''
	Поиск процедур по части наименования или коду процедуры
	'''
	serializer_class = MedProcEnSerializer
	http_method_names = ['post']
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer
	
	@swagger_auto_schema(request_body=MedProcFilterSerializer, responses={201: MedProcRuSerializer,})
		# openapi.Schema(
  #       type=openapi.TYPE_OBJECT,
  #       properties={
  #           'txt': openapi.Schema(type=openapi.TYPE_STRING, description='Часть наименования процедуры или код процедуры'),
  #           'dt': openapi.Schema(type=openapi.TYPE_STRING, description='Выбранный день'),
  #           'doctor_uid': openapi.Schema(type=openapi.TYPE_STRING, description='uid выбранного врача'),
  #       }))
	def post(self, request, *args, **kwargs):
		serializer = MedProcFilterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		sclass = self.get_serializer_class()
		if 'Ru' in str(sclass):
			resSerializer = sclass(MedProc.objects.filter(Q(code__startswith=serializer.data['txt']) | Q(title_ru__icontains=serializer.data['txt']) ), many=True)
		else:
			resSerializer = sclass(MedProc.objects.filter(Q(code__startswith=serializer.data['txt']) | Q(title_en__icontains=serializer.data['txt']) ), many=True)
		#headers = self.get_success_headers(resSerializer.data)
		try:
			logger.info(request.data)
		except:
			pass

		return Response(resSerializer.data, status=status.HTTP_200_OK) #, headers=resSerializer.headers
