from django.db import models
from tree_queries.models import TreeNode
import uuid


class Category(TreeNode):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=20, null=False, blank=False)
	title = models.CharField(max_length=255, null=False, blank=False)
	title_short = models.CharField(max_length=35, null=False, blank=False)
	description = models.TextField(null=True, blank=True)

	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
	def __str__(self):
		return u"{}.{}".format(self.code, self._title_simple())

	def _title_simple( self ):
		return self.title_short if self.title_short else '{}...'.format(self.title_short[:32])
	title_simple = property(_title_simple)
