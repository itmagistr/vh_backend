from django.db import models
from vh_employee.models import Employee
from vh_medproc.models import MedProc
from vh_rating.models import Rating
import uuid

# def doctor_image_upload_to(self, filename):
# 	"""
# 	Compute the upload path for the image field.
# 	"""
# 	filename, extension = os.path.splitext(filename)
# 	return os.path.join(
# 		UPLOAD_TO, '%s%s' % (slugify(filename), extension))

class Special(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	description = models.TextField()
	class Meta:
		verbose_name = 'Специализация'
		verbose_name_plural = 'Специализации'
	def __str__(self):
		return u"{}.{}".format(self.id, self.title)

class Level(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	description = models.TextField()
	class Meta:
		verbose_name = 'Категория врача'
		verbose_name_plural = 'Категории врачей'
	def __str__(self):
		return u"{}.{}".format(self.id, self.title)



class Doctor(Employee):
	special = models.ForeignKey(Special, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Специализация врача', help_text='Укажите специализацию врача', related_name='specDoctors')
	level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Категория врача', help_text='Укажите категорию врача', related_name='levelDoctors')
	youtube = models.URLField(max_length=250, null=True, blank=True, verbose_name='Ссылка на Youtube', help_text='Укажите ссылку на Youtube канал врача')
	
	class Meta:
		verbose_name = 'Врач'
		verbose_name_plural = 'Врачи'


class DoctorMedProc(models.Model):
	doctor = models.ForeignKey(Doctor, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Врач', help_text='Укажите врача')
	medproc = models.ForeignKey(MedProc, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Процедура', help_text='Укажите процедуру, выполняемую выбранным врачом')
	rating = models.ForeignKey(Rating, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Рейтинг процедуры', help_text='Укажите рейтинг процедуры, выполненную врачом')
	class Meta:
		verbose_name = 'Процедура врача'
		verbose_name_plural = 'Процедуры врачей'

	def __str__(self):
		return u"{}.{}".format(self.doctor, self.medproc)

