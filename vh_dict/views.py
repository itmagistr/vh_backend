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



class DictStrListView(generics.RetrieveAPIView):
	'''
	_______________
	'''
	serializer_class = DictStrEnSerializer
	#lookup_field = 'uid'
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DictStrRuSerializer
		return DictStrEnSerializer
		
	def get_queryset(self):
		return DictString.objects.filter(code='COMP')
	def get_object(self):
		obj = get_object_or_404(self.get_queryset())
		return obj


class DictStrFilterView(generics.ListAPIView):
	'''
	___________________________________
	'''
	serializer_class = DictStrEnSerializer
	http_method_names = ['post']
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DictStrRuSerializer
		return DictStrEnSerializer
	
	@swagger_auto_schema(request_body=DictStrFilterSerializer, responses={201: DictStrRuSerializer,})
	def post(self, request, *args, **kwargs):
		serializer = DictStrFilterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		sclass = self.get_serializer_class()
		resSerializer = sclass(DictString.objects.filter(code=serializer.data['code'])[0].descendants(), many=True)
		#logger.info(resSerializer.data)
		#logger.info(dict(resSerializer.data))
		try:
			logger.info(request.data)
		except:
			pass

		return Response({vv['code']:vv for vv in resSerializer.data}, status=status.HTTP_200_OK) #, headers=resSerializer.headers
