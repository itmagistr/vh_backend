from django.db import models
from vh_product.models import Product

class MedProc(Product):
	duration = models.IntegerField(default=30, verbose_name='Продолжительность', help_text='Укажите продолжительность процедуры')
	recomend_before = models.TextField(null=True, blank=True, verbose_name='До процедуры', help_text='Добавьте рекомендации для подготовке к прохождению процедуры')
	recomend_after = models.TextField(null=True, blank=True, verbose_name='После процедуры', help_text='Добавьте рекомендации после прохождения процедуры')
	class Meta:
		verbose_name = 'Процедура'
		verbose_name_plural = 'Процедуры'

	# def __str__(self):
	# 	return u"{}".format(self.title)


