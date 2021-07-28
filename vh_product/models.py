from django.db import models
import uuid
from polymorphic.models import PolymorphicModel
from vh_category.models import Category
from vh_employee.models import Employee

class Product(PolymorphicModel):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=20, null=False, blank=False)
	title = models.CharField(max_length=255, null=False, blank=False)
	title_check = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=10, default=1000, decimal_places=2)
	price_old = models.DecimalField(max_digits=10, default=1000, decimal_places=2)
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
	def __str__(self):
		return u"{}.{}".format(self.code, self.title_check)

	def _product_role( self ):
		return self.__class__.__name__
	product_role = property(_product_role)

class ProductCategory(models.Model):
	product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Продукт', help_text='Укажите продукт из каталога')
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Категория продукта', help_text='Укажите категорию из разделов каталога')
	pos = models.PositiveIntegerField(default=0, verbose_name='Номер по порядку', help_text='Укажите позицию связи для сортировки')
	class Meta:
		verbose_name = 'Связь продукта с категорией'
		verbose_name_plural = 'Категории продукта'
	def __str__(self):
		return u"{}.{}".format(self.category, self.product)

class ProductEmployee(models.Model):
	product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Продукт', help_text='Укажите продукт из каталога', related_name='workers')
	employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Исполнитель', help_text='Веберите исполнителя продукта', related_name='products')
	pos = models.PositiveIntegerField(default=0, verbose_name='Номер по порядку', help_text='Укажите позицию связи для сортировки')
	class Meta:
		verbose_name = 'Связь продукта с исполнителем'
		verbose_name_plural = 'Исполнители продукта'
	def __str__(self):
		return u"{}.{}".format(self.employee, self.product)