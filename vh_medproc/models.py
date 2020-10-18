from django.db import models
from vh_product.models import Product

class MedProc(Product):
	duration = models.IntegerField(default=30)
	class Meta:
		verbose_name = 'Процедура'
		verbose_name_plural = 'Процедуры'

	# def __str__(self):
	# 	return u"{}".format(self.title)


