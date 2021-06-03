from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import *
from vh_product.models import ProductCategory, ProductEmployee
# Register your models here.

class ProdCategoryInline(admin.TabularInline):
	model = ProductCategory
	extra = 1

class ProdEmployeeInline(admin.TabularInline):
	model = ProductEmployee
	extra = 1

class MedProcAdmin(TranslationAdmin):
	model = MedProc
	readonly_fields=('uid',)
	list_display = ('code', 'title', 'price', 'price_old', 'duration', )
	list_display_links = ('code', 'title', 'price')
	search_fields = ('code', 'title', )
	list_filter = ('duration', )
	#ordering = ('code',)
	inlines = [ProdCategoryInline, ProdEmployeeInline]

admin.site.register(MedProc, MedProcAdmin)