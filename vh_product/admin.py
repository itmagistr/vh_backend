from django.contrib import admin
from .models import *
from vh_medproc.models import *

# Register your models here.
class MedProcInline(admin.TabularInline):
	model = MedProc
	extra = 0

class ProductAdmin(admin.ModelAdmin):
	model = Product
	inlines = [MedProcInline,]

admin.site.register(Product, ProductAdmin)
#from modeltranslation.admin import TranslationAdmin
#https://django-modeltranslation.readthedocs.io/en/latest/admin.html#tweaks-applied-to-the-admin