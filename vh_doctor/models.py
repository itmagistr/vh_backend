from django.db import models
from django.contrib.auth.models import User
from vh_doctor.settings import UPLOAD_TO
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
        return u"{}".format(self.title)

class Doctor(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    special = models.ForeignKey(Special, null=True, blank=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    midName = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=16)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=doctor_image_upload_to)
    usr = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    youtube = models.URLField(max_length=250, null=True, blank=True)
	
    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
    def __str__(self):
        return u"{} {} {}".format(self.lastName, self.firstName, self.midName)


