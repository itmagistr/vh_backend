from django.db import models
from vh_client.models import Client
from vh_doctor.models import Doctor
from vh_medproc.models import MedProc
#from vh_orders.models import Invoice
#import datetime as dtime
import uuid
import json
import sys
#from polymorphic.models import PolymorphicModel
import logging
logger = logging.getLogger(__name__)


class TimeSlot(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	dt_start = models.TimeField(verbose_name='время начала промежутка')
	dt_end = models.TimeField(verbose_name='время завершения промежутка')
	descr = models.TextField(null=True, blank=True, verbose_name='описание временного промежутка')
	class Meta:
		verbose_name = 'Временный промежуток'
		verbose_name_plural = 'Временные промежутки'
	def __str__(self):
		return u"{}-{}".format(self.dt_start.strftime("%H:%M"), self.dt_end.strftime("%H:%M"))
	@classmethod
	def get_slots_stats_on_date(cls, dt):
		''' сбор статистики кол-ва записей в день '''
		res = cls.objects.raw("""SELECT vh_booking_timeslot.id, vh_booking_timeslot.dt_start, vh_booking_timeslot.dt_end, sum(
									CASE 
										when time(vh_booking_booking.dt_start) >= vh_booking_timeslot.dt_start 
											and time(vh_booking_booking.dt_start) < vh_booking_timeslot.dt_end then 1
										else 0
									END
										) as cnt_booking
								FROM vh_booking_timeslot
								CROSS JOIN vh_booking_booking 
								WHERE date(vh_booking_booking.dt_start) = %s
								GROUP BY vh_booking_timeslot.dt_start, vh_booking_timeslot.dt_end""", [dt])
		return res
	@classmethod
	def get_slots_colors_on_date(cls, dt):
		''' выдача типа раскраски временных промежутков в указанный день'''
		res = cls.objects.raw("""SELECT vh_booking_timeslot.id, vh_booking_timeslot.dt_start, vh_booking_timeslot.dt_end, CASE sum(
									CASE 
										when time(vh_booking_booking.dt_start) >= vh_booking_timeslot.dt_start 
											and time(vh_booking_booking.dt_start) < vh_booking_timeslot.dt_end then 1
										else 0
									END
										) 
										WHEN 0 THEN 0
										WHEN 1 THEN 1 
										WHEN 2 THEN 2
										WHEN 3 THEN 3
										ELSE 4
										END as status
								FROM vh_booking_timeslot
								CROSS JOIN vh_booking_booking 
								WHERE date(vh_booking_booking.dt_start) = %s
								GROUP BY vh_booking_timeslot.dt_start, vh_booking_timeslot.dt_end""", [dt])
		return res

class Booking(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	dt_start = models.DateTimeField(verbose_name='Дата и время процедуры')
	medproc = models.ForeignKey(MedProc, null=False, blank=False, verbose_name='Процедура', on_delete=models.CASCADE)
	client = models.ForeignKey(Client, null=False, blank=False, verbose_name='Клиент', on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor, null=True, blank=True, verbose_name='Врач', on_delete=models.CASCADE)
	#branch = models.ForeignKey(Branch, null=True, blank=True, verbose_name='Филиал', on_delete=models.CASCADE)
	comment = models.TextField(null=True, blank=True)
	#invoice = models.ForeignKey(Invoice, null=True, blank=True, verbose_name='Счет', on_delete=models.CASCADE)
	dt_create = models.DateTimeField(auto_now_add=True, editable=False)
	#usr_create = models.ForeignKey(Human, null=False, blank=False, editable=False, verbose_name='Пользователь создавший запись', on_delete=models.CASCADE)
	dt_update = models.DateTimeField(auto_now=True, editable=False)
	#usr_update = models.ForeignKey(Human, null=False, blank=False, verbose_name='Пользователь изменивший запись', on_delete=models.CASCADE)
	status = models.PositiveIntegerField(default=0, verbose_name='Статус записи')

	
	class Meta:
		verbose_name = 'Запись на приём'
		verbose_name_plural = 'Записи на приём'
	def __str__(self):
		return u"{}.{}.{}".format(self.dt_start, self.medproc.code, self.client.human_fio)

	@classmethod
	def create_from_json(cls, jsn_str):
		'''
		создание записи на прием из JSON
		'''
		if len(jsn_str)>0:
			logger.info(jsn_str)
			m_jsn = json.loads(jsn_str)
			m_dtStart = m_jsn['dt']
			
			m_medproc = MedProc.objects.get(uid=m_jsn['medproc_uid'])
			m_client = Client.objects.get(uid=m_jsn['client_uid'])
			m_comment = m_jsn['comment']
			try:
				m_doctor = Doctor.objects.get(uid=m_jsn.get('doctor_uid', None))
			except:
				logger.info('doctor_uid {}'.format(sys.exc_info()[0]))
				m_doctor = None
			bk = cls(dt_start=m_dtStart, medproc=m_medproc, client=m_client, comment=m_comment, doctor=m_doctor)
		
		return bk