from django.contrib import admin
from .models import Human
from modeltranslation.admin import TranslationAdmin


class HumanAdmin(TranslationAdmin):
	model = Human
	readonly_fields=('uid',)

admin.site.register(Human, HumanAdmin)