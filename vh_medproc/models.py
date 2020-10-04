from django.db import models
import uuid

class MedProc(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	description = models.TextField()
	duration = models.IntegerField(default=30)
	class Meta:
		verbose_name = 'Процедура'
		verbose_name_plural = 'Процедуры'

	def __str__(self):
		return u"{}".format(self.title)


