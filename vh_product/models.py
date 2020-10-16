from django.db import models
import uuid
from polymorphic.models import PolymorphicModel

class Product(PolymorphicModel):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=20, null=False, blank=False)
	title = models.CharField(max_length=255, null=False, blank=False)
	title_check = models.CharField(max_length=55, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=10, default=1000, decimal_places=2)
	price_old = models.DecimalField(max_digits=10, default=1000, decimal_places=2)
	
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
	def __str__(self):
		return u"{}.{}".format(self.code, self.title_check)

	