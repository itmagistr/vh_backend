from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import *
# Register your models here.


class MedProcAdmin(TranslationAdmin):
	model = MedProc
	readonly_fields=('uid',)

admin.site.register(MedProc, MedProcAdmin)