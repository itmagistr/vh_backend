from django.db import models
from vh_human.models import Human
import uuid

def doctor_image_upload_to(self, filename):
	"""
	Compute the upload path for the image field.
	"""
	filename, extension = os.path.splitext(filename)
	return os.path.join(
		UPLOAD_TO, '%s%s' % (slugify(filename), extension))

class Special(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	description = models.TextField()
	class Meta:
		verbose_name = 'Специализация'
		verbose_name_plural = 'Специализации'
	def __str__(self):
		return u"{}.{}".format(self.id, self.title)

class Doctor(models.Model):
	human = models.ForeignKey(Human, null=False, blank=False, on_delete=models.CASCADE)
	special = models.ForeignKey(Special, null=True, blank=True, on_delete=models.CASCADE)
	youtube = models.URLField(max_length=250, null=True, blank=True)
	
	class Meta:
		verbose_name = 'Врач'
		verbose_name_plural = 'Специальные поля Врача'
	def __str__(self):
		return u"{} {} {}".format(self.human.lastName, self.human.firstName, self.human.midName)


