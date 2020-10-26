from django.db import models
import uuid
from polymorphic.models import PolymorphicModel
# Create your models here.

class Rating(PolymorphicModel):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	rate = models.IntegerField(default=0)
	title = models.CharField(max_length=255)
	description = models.TextField()
	class Meta:
		verbose_name = 'Рейтинг'
		verbose_name_plural = 'Рейтинги'
	def __str__(self):
		return u"{}.{}".format(self.id, self.title)