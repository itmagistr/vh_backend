from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.utils import translation
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging
logger = logging.getLogger(__name__)
# Create your views here.

class DoctorListView(generics.RetrieveAPIView):
	'''
	Получить дежурного врача
	'''
	serializer_class = DoctorEnSerializer
	lookup_field = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DoctorRuSerializer
		return DoctorEnSerializer
		
	def get_queryset(self):
		return Doctor.objects.filter(id=1)
	def get_object(self):
		obj = get_object_or_404(self.get_queryset())
		return obj

class DoctorView(generics.RetrieveAPIView):
	'''
	Получить процедуру по uid.
	'''
	serializer_class = DoctorEnSerializer
	lookup_field = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DoctorRuSerializer
		return DoctorEnSerializer
		
	def get_queryset(self):
		return Doctor.objects.all()

class DoctorFilterView(generics.ListAPIView):
	'''
	Поиск процедур по части наименования или коду процедуры
	'''
	serializer_class = DoctorEnSerializer
	http_method_names = ['post']
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DoctorRuSerializer
		return DoctorEnSerializer
	
	@swagger_auto_schema(request_body=DoctorFilterSerializer, responses={201: DoctorRuSerializer,})
	def post(self, request, *args, **kwargs):
		serializer = DoctorFilterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		sclass = self.get_serializer_class()
		if 'Ru' in str(sclass):
			resSerializer = sclass(Doctor.objects.filter(Q(lastName_ru__icontains=serializer.data['txt']) | Q(firstName_ru__icontains=serializer.data['txt']) ), many=True)
		else:
			resSerializer = sclass(Doctor.objects.filter(Q(lastName_en__icontains=serializer.data['txt']) | Q(firstName_en__icontains=serializer.data['txt']) ), many=True)
		#headers = self.get_success_headers(resSerializer.data)
		return Response(resSerializer.data, status=status.HTTP_200_OK) #, headers=resSerializer.headers
