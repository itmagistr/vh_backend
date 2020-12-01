from django.db import models
from django.contrib.auth.models import User
from vh_human.settings import UPLOAD_TO
import uuid
import os
from django.utils.text import slugify

from polymorphic.models import PolymorphicModel
from vh_rating.models import Rating

def image_upload_to(self, filename):
	"""
	Compute the upload path for the image field.
	"""
	filename, extension = os.path.splitext(filename)
	return os.path.join(
		UPLOAD_TO, '%s%s' % (slugify(filename), extension))

class Human(PolymorphicModel):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	#title = models.CharField(max_length=255)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	midName = models.CharField(max_length=50, null=True, blank=True)
	phone = models.CharField(max_length=16, null=True, blank=True)
	
	
	usr = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True, upload_to=image_upload_to)
	rating = models.ForeignKey(Rating, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Рейтинг', help_text='Укажите рейтинг')
	class Meta:
		verbose_name = 'Персона'
		verbose_name_plural = 'Персоны'
	def __str__(self):
		res = "{} {} {}".format(self.lastName, self.firstName, self.midName if self.midName else '') 
		return res if len(res) > 3 else '{} {}'.format(self.uid, self.phone)

	def _human_role( self ):
		return self.__class__.__name__
	human_role = property(_human_role)


	def _human_fio( self ):
		return "{} {} {}".format(self.lastName, self.firstName, self.midName if self.midName else '') 
	human_fio = property(_human_fio)