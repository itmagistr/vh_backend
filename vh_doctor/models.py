from django.db import models
from vh_employee.models import Employee
from vh_category.models import Category
from vh_medproc.models import MedProc
from vh_rating.models import Rating
from vh_doctor.settings import UPLOAD_TO
import uuid
import os
from django.utils.text import slugify
import datetime
from dateutil.relativedelta import relativedelta

def image_upload_to(self, filename):
	"""
	Compute the upload path for the image field.
	"""
	filename, extension = os.path.splitext(filename)
	return os.path.join(
		UPLOAD_TO, '%s%s' % (slugify(filename), extension))

class Special(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=25)
	title = models.CharField(max_length=255)
	description = models.TextField()
	img =  models.ImageField(null=True, blank=True, upload_to=image_upload_to)
	class Meta:
		verbose_name = 'Специализация'
		verbose_name_plural = 'Специализации'
	def __str__(self):
		return u"{}.{}".format(self.id, self.title)

class Level(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=25)
	title = models.CharField(max_length=255)
	description = models.TextField()
	class Meta:
		verbose_name = 'Категория врача'
		verbose_name_plural = 'Категории врачей'
	def __str__(self):
		return u"{}.{}".format(self.id, self.title)

class Degree(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=25)
	title = models.CharField(max_length=255)
	description = models.TextField()
	class Meta:
		verbose_name = 'Ученая степень'
		verbose_name_plural = 'Ученые степени'
	def __str__(self):
		return u"{}.{}".format(self.id, self.title)


class Doctor(Employee):
	special = models.ForeignKey(Special, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Специализация врача', help_text='Укажите специализацию врача', related_name='specDoctors')
	level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Категория врача', help_text='Укажите категорию врача', related_name='levelDoctors')
	degree = models.ForeignKey(Degree, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Ученая степень', help_text='Укажите ученую степень если есть', related_name='degreeDoctors')
	dt_practic = models.DateField(default=datetime.datetime.now()-relativedelta(years=3), verbose_name='Дата начала практики', help_text='Укажите дату начала медецинской практики')
	сertificate = models.TextField(null=True, blank=True, verbose_name='Сертификат', help_text='Укажите информацию о сертификате врача')
	youtube = models.URLField(max_length=250, null=True, blank=True, verbose_name='Ссылка на Youtube', help_text='Укажите ссылку на Youtube канал врача')
	fb = models.URLField(max_length=250, null=True, blank=True, verbose_name='Ссылка на Facebook', help_text='Укажите ссылку на Facebook канал врача')
	vk = models.URLField(max_length=250, null=True, blank=True, verbose_name='Ссылка на ВКонтакте', help_text='Укажите ссылку на ВКонтакте канал врача')
	insta = models.URLField(max_length=250, null=True, blank=True, verbose_name='Ссылка на Instagram', help_text='Укажите ссылку на Instagram канал врача')
	education = models.TextField(null=True, blank=True, verbose_name='Образование', help_text='Укажите информацию об образовании врача')
	class Meta:
		verbose_name = 'Врач'
		verbose_name_plural = 'Врачи'
	def _experience(self):
		return relativedelta(datetime.datetime.now(), self.dt_practic).years
	experience = property(_experience)
	def _special_ru_str(self):
		specs = DocCategory.objects.filter(doctor=self).order_by('pos')[:2]
		return '-'.join([s.category.title_ru for s in specs])
	special_ru_str = property(_special_ru_str)
	def _special_en_str(self):
		specs = DocCategory.objects.filter(doctor=self).order_by('pos')[:2]
		return '-'.join([s.category.title_en for s in specs])
	special_en_str = property(_special_en_str)

# заменена на ProductEmployee
class DoctorMedProc(models.Model):
	doctor = models.ForeignKey(Doctor, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Врач', help_text='Укажите врача', related_name='medprocs')
	medproc = models.ForeignKey(MedProc, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Процедура', help_text='Укажите процедуру, выполняемую выбранным врачом')
	rating = models.ForeignKey(Rating, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Рейтинг процедуры', help_text='Укажите рейтинг процедуры, выполненную врачом')
	class Meta:
		verbose_name = 'Процедура врача'
		verbose_name_plural = 'Процедуры врачей'

	def __str__(self):
		return u"{}.{}".format(self.doctor, self.medproc)

class DocWorkRes(models.Model):
	doctor = models.ForeignKey(Doctor, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Врач', help_text='Укажите врача')
	img = models.ImageField(null=False, blank=False, verbose_name='Фото', help_text='Выбор изображения результата работы')
	title = models.CharField(null=True, blank=True, max_length=255)
	pos = models.PositiveIntegerField(default=0, verbose_name='Номер по порядку', help_text='Укажите позицию связи для сортировки')
	class Meta:
		verbose_name = 'Фото работы врача'
		verbose_name_plural = 'Фото работ врачей'

	def __str__(self):
		return u"{}.{}.{}".format(self.doctor, self.pos, self.img.name)

class DocCategory(models.Model):
	doctor = models.ForeignKey(Doctor, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Врач', help_text='Укажите врача')
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Специализация', help_text='Укажите специализацию врача из разделов каталога')
	pos = models.PositiveIntegerField(default=0, verbose_name='Номер по порядку', help_text='Укажите позицию для сортировки')
	class Meta:
		verbose_name = 'Связь врача со специализацией'
		verbose_name_plural = 'Специализации врачей'
	def __str__(self):
		return u"{}.{}.{}".format(self.pos, self.category, self.doctor)