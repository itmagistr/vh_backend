from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
	model = Category
	readonly_fields = ['uid']

admin.site.register(Category, CategoryAdmin)

