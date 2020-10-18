from django.contrib.auth.models import User, Group
from vh_medproc.models import *
from vh_doctor.models import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from .serializers import *
import random
import datetime
from vh_medproc.serializers import *
from vh_doctor.serializers import *
from django.utils import translation
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


class MedProcViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = MedProcEnSerializer
	http_method_names = ['get']
	def get_serializer_class(self):
		logger.info(translation.get_language())

		if 'ru' in translation.get_language():
			# using 'in' because it can be set to something like 'es-ES; es'
			return MedProcRuSerializer
		return MedProcEnSerializer
		
	def get_queryset(self):
		return MedProc.objects.all()


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
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

class DayStatusView(generics.ListAPIView):
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
	serializer_class = TimeStatusSerializer
	
	def get_queryset(self):
		"""
		раскраска временных слотов
		"""
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
