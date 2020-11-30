from django.db import models
from tree_queries.models import TreeNode
import uuid

class FeedbackType(models.Model):
	code = models.CharField(max_length=16, null=False, blank=False, verbose_name='Код обратной связи', help_text='Укажите код обратной связи латинскими символами. CODE_CALL, CODE_FB')
	title = models.CharField(max_length=30, null=False, blank=False)
	class Meta:
		verbose_name = 'Вид обратной связи'
		verbose_name_plural = 'Виды обратной связи'
	def __str__(self):
		return self.code

class Feedback(models.Model):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	fb_type = models.ForeignKey(FeedbackType, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Вид обратной связи', help_text='Укажите вид обратной связи')
	name = models.CharField(max_length=150, null=False, blank=False)
	phone = models.CharField(max_length=20, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	call_hr = models.PositiveIntegerField(null=True, blank=True)
	call_mn = models.PositiveIntegerField(null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	class Meta:
		verbose_name = 'Обратная связь'
		verbose_name_plural = 'Журнал обратной связи и звонков'
	def __str__(self):
		return '{}'.format(self.uid)
		# return self._title_simple()

	def _title_simple( self ):
		return '{}...'.format(self.title[:32])
	title_simple = property(_title_simple)
