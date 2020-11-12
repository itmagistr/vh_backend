from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import *
from .models import Booking
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import logging
logger = logging.getLogger(__name__)


class BookingView(generics.RetrieveAPIView):
	'''
	Просмотреть существующее бронирование времени приема по uid.
	'''
	serializer_class = BookingSerializer
	lookup_field = 'uid'
	# def get_serializer_class(self):
	# 	logger.info(translation.get_language())

	# 	if 'ru' in translation.get_language():
	# 		# using 'in' because it can be set to something like 'es-ES; es'
	# 		return MedProcRuSerializer
	# 	return MedProcEnSerializer
		
	def get_queryset(self):
		return Booking.objects.all()


class BookingFilterView(generics.ListAPIView):
	'''
	Поиск существующих бронирований времени приема по времени начала или части названия процедуры
	'''
	serializer_class = BookingSerializer
	http_method_names = ['post']
	# def get_serializer_class(self):
	# 	logger.info(translation.get_language())

	# 	if 'ru' in translation.get_language():
	# 		# using 'in' because it can be set to something like 'es-ES; es'
	# 		return MedProcRuSerializer
	# 	return MedProcEnSerializer
	
	@swagger_auto_schema(request_body=BookingFilterSerializer, responses={200: BookingSerializer,})
	def post(self, request, *args, **kwargs):
		serializer = BookingFilterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		sclass = self.get_serializer_class()
		logging.info('request user is {}'.format(request.user))
		#resSerializer = sclass(Booking.objects.filter(Q(client__uid=serializer.data['client_uid']), Q(dt_start=serializer.data['dt_start']) | Q(medproc__title__icontains=serializer.data['txt']) | Q(medproc__uid=serializer.data['medproc_uid']) | Q(doctor__uid=serializer.data['doctor_uid']) ), many=True)
		resSerializer = sclass(Booking.objects.filter(Q(dt_start=serializer.data['dt_start']) | Q(medproc__title__icontains=serializer.data['txt'])  ), many=True)
		#headers = self.get_success_headers(resSerializer.data)
		return Response(resSerializer.data, status=status.HTTP_200_OK) #, headers=resSerializer.headers
