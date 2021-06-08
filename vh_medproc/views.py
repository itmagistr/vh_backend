from django.shortcuts import render
#from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.utils import translation
from .serializers import *
from vh_doctor.serializers import *
from vh_product.models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from vh_product.models import ProductCategory
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
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer
		
	def get_queryset(self):
		return MedProc.objects.filter(code='CLV01')
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
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer
		
	def get_queryset(self):
		return MedProc.objects.all()

class MedProcLightView(generics.RetrieveAPIView):
	'''
	Получить процедуру по uid с ограниченным набором полей.
	'''
	serializer_class = MedProcLightEnSerializer
	lookup_field = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcLightRuSerializer
		return MedProcLightEnSerializer
		
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
	serializer_class = MedProcLightEnSerializer
	http_method_names = ['post']
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcLightRuSerializer
		return MedProcLightEnSerializer
	
	@swagger_auto_schema(request_body=MedProcFilterSerializer, responses={200: MedProcLightRuSerializer,})
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
		if len(serializer.data['category']) > 0:
			categories = [ c["code"] for c in serializer.data['category']]
			resQ = [el.product for el in ProductCategory.objects.filter(category__code__in=categories).order_by('pos')]
		elif len(serializer.data['txt']) ==0:
			#resQ = MedProc.objects.filter(code__startswith='CLV')
			resQ = [el.product for el in ProductCategory.objects.filter(category__code='PRE_BOOKING').order_by('pos')]
		else:

			if 'Ru' in str(sclass):
				resQ = MedProc.objects.filter(Q(code__startswith=serializer.data['txt']) | Q(title_ru__icontains=serializer.data['txt']) )
			else:
				resQ = MedProc.objects.filter(Q(code__startswith=serializer.data['txt']) | Q(title_en__icontains=serializer.data['txt']) )
		#headers = self.get_success_headers(resSerializer.data)
		if len(resQ)==0:
			resQ = MedProc.objects.filter(code__startswith='CLV')
		try:
			resSerializer = sclass(resQ[:20], many=True)
			logger.info(request.data)
		except:
			pass

		return Response(resSerializer.data, status=status.HTTP_200_OK) #, headers=resSerializer.headers


class MedProcDoctorsView(generics.ListAPIView):
	'''
	Список докторов выполняющих процедуру
	'''
	serializer_class = DoctorLightRuSerializer
	lookup_url_kwarg = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DoctorLightRuSerializer
		return DoctorLightEnSerializer
		
	def get_queryset(self):
		uid = self.kwargs.get(self.lookup_url_kwarg)
		resQ = [el.employee for el in Product.objects.filter(uid=uid)[0].workers.all()]
		return resQ


class MedProcSearchView(generics.ListAPIView):
	serializer_class = MedProcEnSerializer
	http_method_names = ['post']
	
	def get_serializer_class(self):
		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer

	@swagger_auto_schema(request_body=MedProcSearchSerializer, responses={201: MedProcRuSerializer,})
	def post(self, request, *args, **kwargs):
		serializer = MedProcSearchSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		sclass = self.get_serializer_class()
		if len(serializer.data['q']) ==0:
			resQ = MedProc.objects.filter(code__startswith='CLV')
		else:
			if 'Ru' in str(sclass):
				resQ = MedProc.objects.filter(Q(code__startswith=serializer.data['q']) | Q(title_ru__icontains=serializer.data['q']) )
			else:
				resQ = MedProc.objects.filter(Q(code__startswith=serializer.data['q']) | Q(title_en__icontains=serializer.data['q']) )
		try:
			resSerializer = sclass(resQ[:20], many=True)
		except:
			pass
		return Response(resSerializer.data, status=status.HTTP_200_OK)