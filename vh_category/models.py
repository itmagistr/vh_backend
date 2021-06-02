from django.db import models
from tree_queries.models import TreeNode
from vh_category.settings import UPLOAD_TO
import os
import uuid
from django.utils.text import slugify

def image_upload_to(self, filename):
	"""
	Compute the upload path for the image field.
	"""
	filename, extension = os.path.splitext(filename)
	return os.path.join(
		UPLOAD_TO, '%s%s' % (slugify(filename), extension))

class Category(TreeNode):
	uid = models.UUIDField(default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=20, null=False, blank=False)
	title = models.CharField(max_length=255, null=False, blank=False)
	title_short = models.CharField(max_length=35, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	img =  models.ImageField(null=True, blank=True, upload_to=image_upload_to)

	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
	def __str__(self):
		return u"{}.{}".format(self.code, self._title_simple())

	def _title_simple( self ):
		return self.title_short if self.title_short else '{}...'.format(self.title_short[:32])
	title_simple = property(_title_simple)
