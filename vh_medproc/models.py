from django.db import models
from vh_product.models import Product

class MedProc(models.Model):
	product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
	duration = models.IntegerField(default=30)
	class Meta:
		verbose_name = 'Процедура'
		verbose_name_plural = 'Специальные поля Процедуры'

	def __str__(self):
		return u"{}".format(self.product.title)


