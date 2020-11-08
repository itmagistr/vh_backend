from django.db import models
from vh_human.models import Human

class Client(Human):

	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'

	def __str__(self):
		res = "{} {}".format(self.human_role, super().__str__()) 
		return res
