from django.contrib import admin
from .models import *
from vh_medproc.models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.
# class MedProcInline(admin.TabularInline):
# 	model = MedProc
# 	extra = 0

class ProductAdmin(TranslationAdmin):
	model = Product
	readonly_fields=('uid',)
	list_display = ('code', 'title', 'price', 'price_old',  )
	list_display_links = ('code', 'title', 'price')
	search_fields = ('code', 'title', )
	list_filter = ('price', )
	ordering = ('code',)


admin.site.register(Product, ProductAdmin)
#from modeltranslation.admin import TranslationAdmin
#https://django-modeltranslation.readthedocs.io/en/latest/admin.html#tweaks-applied-to-the-admin