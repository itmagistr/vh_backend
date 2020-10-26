from django.db import models
import uuid
from vh_human.models import Human
# Create your models here.

class EmpRole(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	description = models.TextField()
	class Meta:
		verbose_name = 'Роль сотрудника'
		verbose_name_plural = 'Роли сотрудников'
	def __str__(self):
		return '{} {}'.format(self.id, self.title)

class Employee(Human):
	empNum = models.CharField(max_length=20, null=True, blank=True)
	empRole = models.ForeignKey(EmpRole, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Роль сотрудника', help_text='Укажите роль сотрудника в организации')

	class Meta:
		verbose_name = 'Сотрудник'
		verbose_name_plural = 'Сотрудники'
	def __str__(self):
		res = "{} {} {}".format(self.empNum if self.empNum else '', self.human_role, super().__str__()) 
		return res

