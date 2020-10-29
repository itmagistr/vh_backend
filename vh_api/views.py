from django.contrib.auth.models import User, Group
from vh_medproc.models import *
from vh_doctor.models import *
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
import random
import datetime
from vh_medproc.serializers import *
from vh_doctor.serializers import *
from django.utils import translation
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging
logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]
	http_method_names = ['get']

	def get_queryset(self):
		return User.objects.all().order_by('-date_joined')

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]
	http_method_names = ['get']
	
	def get_queryset(self):
		return Group.objects.all()


class DayStatusView(generics.ListAPIView):
	"""
	Получить раскраску дней - перейти на использование /timeslot/day/list
	"""
	serializer_class = DayStatusSerializer
	
	def get_queryset(self):
		"""
		раскраска дней
		"""
		dstart = self.kwargs['dstart']
		dend = self.kwargs['dend']
		ds = datetime.datetime.fromisoformat(dstart)
		de = datetime.datetime.fromisoformat(dend)
		nlen = abs((de-ds).days)+1
		lst = random.choices([1,2,3], weights = [5, 10, 5], k = nlen)

		return [{'d': (ds + datetime.timedelta(days=el)).strftime('%Y-%m-%d'), 's': lst[el]} for el in range(nlen)]


class TimeStatusView(generics.ListAPIView):
	"""
	Получить раскраску времени для желаемой даты - перейти на использование /timeslot/list
	"""
	serializer_class = TimeStatusSerializer
	
	def get_queryset(self):
		
		d = self.kwargs['d']
		
		dt = datetime.datetime.fromisoformat(d)
		tlst = ['06:00', '06:30','07:00','07:30',
				'08:00', '08:30','09:00','09:30',
				'10:00', '10:30','11:00','11:30',
				'12:00', '12:30','13:00','13:30',
				'14:00', '14:30','15:00','15:30',
				'16:00', '16:30','17:00','17:30',
				'18:00', '18:30','19:00','19:30',
				'20:00', '20:30','21:00','21:30',
				'22:00', '22:30','23:00','23:30',]
		nlen = len(tlst)
		lst = random.choices([1,2,3], weights = [5, 10, 5], k = nlen)

		return [{'t': tlst[el], 's': lst[el]} for el in range(nlen)]




class TimeSlotDayView(APIView):
	'''
	Получить ближайший день на который открыта запись
	'''
	serializer_class = LuckyDaySerializer
	@swagger_auto_schema(responses={200: LuckyDaySerializer,})
	def get(self, request, *args):
		res = LuckyDaySerializer(data={'dt': datetime.datetime.today().isoformat()[0:10]})
		res.is_valid(raise_exception=True)
		return Response(res.data, status=status.HTTP_200_OK) 

class TimeSlotDayListView(generics.ListAPIView):
	'''
	Получить раскраску дней
	'''
	serializer_class = DayStatusSerializer
	http_method_names = ['post']
	@swagger_auto_schema(request_body=PeriodSerializer, responses={200: DayStatusSerializer,})
	def post(self, request, *args):
		serializer = PeriodSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		ds = datetime.datetime.fromisoformat(serializer.data['dstart'])
		de = datetime.datetime.fromisoformat(serializer.data['dend'])
		nlen = abs((de-ds).days)+1
		lst = random.choices([1,2,3], weights = [5, 10, 5], k = nlen)
		
		res = DayStatusSerializer(data=[{'d': (ds + datetime.timedelta(days=el)).strftime('%Y-%m-%d'), 's': lst[el]} for el in range(nlen)],  many=True)
		res.is_valid()
		return Response(res.data, status=status.HTTP_200_OK) 

class TimeSlotListView(generics.ListAPIView):
	'''
	Получить раскраску времени для желаемой процедуры, врача, даты
	'''
	serializer_class = TimeStatusSerializer
	http_method_names = ['post']
	@swagger_auto_schema(request_body=DaySerializer, responses={200: TimeStatusSerializer,})
	def post(self, request, *args, **kwargs):
		serializer = DaySerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		dt = datetime.datetime.fromisoformat(serializer.data['dt'])
		tlst = ['06:00', '06:30','07:00','07:30',
				'08:00', '08:30','09:00','09:30',
				'10:00', '10:30','11:00','11:30',
				'12:00', '12:30','13:00','13:30',
				'14:00', '14:30','15:00','15:30',
				'16:00', '16:30','17:00','17:30',
				'18:00', '18:30','19:00','19:30',
				'20:00', '20:30','21:00','21:30',
				'22:00', '22:30','23:00','23:30',]
		nlen = len(tlst)
		lst = random.choices([1,2,3], weights = [5, 10, 5], k = nlen)

		res = TimeStatusSerializer(data=[{'t': tlst[el], 's': lst[el]} for el in range(nlen)], many=True)
		res.is_valid(raise_exception=True)
		return Response(res.data, status=status.HTTP_200_OK) 