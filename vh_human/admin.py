from django.contrib import admin
from .models import Human
from modeltranslation.admin import TranslationAdmin


class HumanAdmin(TranslationAdmin):
	model = Human

admin.site.register(Human, HumanAdmin)