from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class DictStringAdmin(TranslationAdmin):
	model = DictString
	#readonly_fields = ['uid']

admin.site.register(DictString, DictStringAdmin)
