from django.shortcuts import render
from rest_framework import viewsets
from django.utils import translation
from .serializers import *
import logging
logger = logging.getLogger(__name__)
# Create your views here.


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
	'''
	Получить дежурного врача
	'''
	serializer_class = DoctorRuSerializer
	http_method_names = ['get']
	
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DoctorRuSerializer
		return DoctorEnSerializer

	def get_queryset(self):
		return Doctor.objects.all()