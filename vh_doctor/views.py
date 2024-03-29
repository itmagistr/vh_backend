from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.utils import translation
from .serializers import *
from vh_medproc.serializers import *
from vh_product.models import *
from vh_category.models import Category
from vh_category.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import random
import logging
logger = logging.getLogger(__name__)
# Create your views here.

class DoctorListView(generics.RetrieveAPIView):
	'''
	Получить дежурного врача
	'''
	serializer_class = DoctorEnSerializer
	#lookup_field = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DoctorRuSerializer
		return DoctorEnSerializer
		
	def get_queryset(self):
		return Doctor.objects.filter(id=1)
	def get_object(self):
		max_id = Doctor.objects.order_by('-id')[0].id
		random_id = random.randint(1, max_id)
		obj = Doctor.objects.filter(id__gte=random_id)[0]
		#obj = get_object_or_404(self.get_queryset())
		return obj

class DoctorView(generics.RetrieveAPIView):
	'''
	Получить доктора по uid.
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
	Поиск врачей по части наименования или кодам специализации
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
		speclist = []
		if len(serializer.data['spec']) > 0:
			speclist = [s["code"] for s in serializer.data['spec']]


		if 'Ru' in str(sclass):
			# if len(serializer.data['medproc_uid']) > 0:
			# 	docs = [e.id for e in MedProc.objects.get(uid=serializer.data['medproc_uid']).workers.all()]
			# 	resQSet = Doctor.objects.filter(id__in=docs)
			# elif
			if len(speclist) > 0:
				resQSet = Doctor.objects.filter(Q(special__code__in=speclist), Q(lastName_ru__icontains=serializer.data['txt']) | Q(firstName_ru__icontains=serializer.data['txt']) )
			else:
				resQSet = Doctor.objects.filter(Q(lastName_ru__icontains=serializer.data['txt']) | Q(firstName_ru__icontains=serializer.data['txt']) )
		else:
			if len(speclist) > 0:
				resQSet = Doctor.objects.filter(Q(special__code__in=speclist), Q(lastName_en__icontains=serializer.data['txt']) | Q(firstName_en__icontains=serializer.data['txt']) )
			else:
				resQSet = Doctor.objects.filter(Q(lastName_en__icontains=serializer.data['txt']) | Q(firstName_en__icontains=serializer.data['txt']) )
		if len(resQSet)==0:
			resQSet = Doctor.objects.filter(id=7)
		resSerializer = sclass(resQSet, many=True)
		#headers = self.get_success_headers(resSerializer.data)
		return Response(resSerializer.data, status=status.HTTP_200_OK) #, headers=resSerializer.headers


class DoctorFilterViewV2(generics.ListAPIView):
	'''
	v.2.Поиск врачей по части наименования или кодам специализации
	'''
	serializer_class = DocSpecRuSerializer
	http_method_names = ['post']
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DocSpecRuSerializer
		return DocSpecEnSerializer
	
	@swagger_auto_schema(request_body=DoctorFilterSerializer, responses={201: DocSpecRuSerializer,})
	def post(self, request, *args, **kwargs):
		serializer = DoctorFilterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		sclass = self.get_serializer_class()
		speclist = []
		if len(serializer.data['spec']) > 0:
			speclist = [s["code"] for s in serializer.data['spec']]


		if 'Ru' in str(sclass):
			# if len(serializer.data['medproc_uid']) > 0:
			# 	docs = [e.id for e in MedProc.objects.get(uid=serializer.data['medproc_uid']).workers.all()]
			# 	resQSet = Doctor.objects.filter(id__in=docs)
			# elif
			if len(speclist) > 0:
				resQSet = DocCategory.objects.filter(Q(category__code__in=speclist), Q(doctor__lastName_ru__icontains=serializer.data['txt']) | Q(doctor__firstName_ru__icontains=serializer.data['txt']) )
			else:
				resQSet = DocCategory.objects.filter(Q(doctor__lastName_ru__icontains=serializer.data['txt']) | Q(doctor__firstName_ru__icontains=serializer.data['txt']) )
		else:
			if len(speclist) > 0:
				resQSet = DocCategory.objects.filter(Q(category__code__in=speclist), Q(doctor__lastName_en__icontains=serializer.data['txt']) | Q(doctor__firstName_en__icontains=serializer.data['txt']) )
			else:
				resQSet = DocCategory.objects.filter(Q(doctor__lastName_en__icontains=serializer.data['txt']) | Q(doctor__firstName_en__icontains=serializer.data['txt']) )
		if len(resQSet)==0:
			resQSet = DocCategory.objects.filter(doctor__lastName_en__icontains='Braginsk')
		docsPK = []
		doctors = []
		for r in resQSet:
			if r.doctor.id not in docsPK:
				docsPK.append(r.doctor.id)
				doctors.append(r)
		resSerializer = sclass(doctors, many=True)
		#headers = self.get_success_headers(resSerializer.data)
		return Response(resSerializer.data, status=status.HTTP_200_OK) #, headers=resSerializer.headers

class SpecListView(generics.ListAPIView):
	'''
	Получить список специализаций врачей
	'''
	serializer_class = CategoryDocSpecEnSerializer #SpecialCodeEnSerializer
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return CategoryDocSpecRuSerializer #SpecialCodeRuSerializer
		return CategoryDocSpecEnSerializer #SpecialCodeEnSerializer
		
	def get_queryset(self):
		#return Special.objects.all()
		return Category.objects.filter(parent__code__exact='DOCSPEC')
	

class DocWorkResView(generics.ListAPIView):
	'''
	Получить фото результатов врача
	'''
	serializer_class = DoctorWorkResSerializer
	#lookup_field = 'uid'
	lookup_url_kwarg = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return DoctorWorkResSerializer
		return DoctorWorkResSerializer
		
	def get_queryset(self):
		uid = self.kwargs.get(self.lookup_url_kwarg)
		return DocWorkRes.objects.filter(doctor__uid=uid)


class DoctorMedProcsView(generics.ListAPIView):
	'''
	Список процедур выполняемые врачом
	'''
	serializer_class = MedProcLightRuSerializer
	lookup_url_kwarg = 'uid'
	def get_serializer_class(self):
		#logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcLightRuSerializer
		return MedProcLightEnSerializer
		
	def get_queryset(self):
		uid = self.kwargs.get(self.lookup_url_kwarg)
		resQ = [el.product for el in Employee.objects.filter(uid=uid)[0].products.all()]
		return resQ