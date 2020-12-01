from django.db import models
import uuid
from polymorphic.models import PolymorphicModel
# Create your models here.

class Rating(PolymorphicModel):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	rate = models.DecimalField(max_digits=5, decimal_places=1, default=4, verbose_name='Рейтинг', help_text='Укажите значение от нуля до пяти с точночтью до десятых')
	title = models.CharField(max_length=255, verbose_name='Отображаемое наименование', help_text='Укажите отображаемое наименование')
	description = models.TextField(verbose_name='Описание рейтинга', help_text='Опишите, что означает значение рейтинга')
	class Meta:
		verbose_name = 'Рейтинг'
		verbose_name_plural = 'Рейтинги'
	def __str__(self):
		return u"{} {}".format(self.rate, self.title)