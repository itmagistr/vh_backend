from django.db import models
from vh_human.models import Human

class Client(Human):

	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'
