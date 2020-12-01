from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class RatingAdmin(TranslationAdmin):
	model = Rating
	readonly_fields=('uid',)
admin.site.register(Rating, RatingAdmin)
