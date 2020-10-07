from django.db import models
from django.contrib.auth.models import User
from vh_human.settings import UPLOAD_TO
import uuid


def image_upload_to(self, filename):
	"""
	Compute the upload path for the image field.
	"""
	filename, extension = os.path.splitext(filename)
	return os.path.join(
		UPLOAD_TO, '%s%s' % (slugify(filename), extension))

class Human(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    midName = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    
    image = models.ImageField(null=True, blank=True, upload_to=image_upload_to)
    usr = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
    def __str__(self):
        return u"{} {} {}".format(self.lastName, self.firstName, self.midName if self.midName else '')
