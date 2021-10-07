from django.contrib import admin
from .models import *
from treebeard.admin import TreeAdmin
from modeltranslation.admin import TranslationAdmin
from treebeard.forms import movenodeform_factory



class CategoryAdmin(TreeAdmin):
	model = Category
	form = movenodeform_factory(Category)
	readonly_fields = ['uid']

admin.site.register(Category, CategoryAdmin)
