from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import *
from vh_product.models import ProductCategory, ProductEmployee
from django.http import HttpResponse
import csv
from io import StringIO
import datetime

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
	ordering = ('code',)
	inlines = [ProdCategoryInline, ProdEmployeeInline]
	actions = ["export_medprocs", ]
	def export_medprocs(self, request, queryset):
		f = StringIO()
		writer = csv.writer(f, delimiter=str(';'))
		writer.writerow(u'\ufeff')
		writer.writerow([u"medproc_id", u"medproc_uid", u"medproc_code", u"title_check_ru", u"title_check_en", u"price", u"price_old", u"duration",
						u"PRE_BOOKING", u"ORTHO", u"SURGEON", u"THERAPY", u"WHITE", u"PROSTHET", u"IMPLANT"])
		for s in MedProc.objects.all().order_by('code'):
			procat = {"PRE_BOOKING": 0, "ORTHO": 0, "SURGEON": 0, "THERAPY": 0, "WHITE": 0, "PROSTHET": 0, "IMPLANT": 0, }
			for pc in ProductCategory.objects.filter(product=s):
				procat[pc.category.code] = 1
			writer.writerow([s.id, s.uid, s.code, s.title_check_ru, s.title_check_en, int(s.price), int(s.price_old), s.duration, 
							procat["PRE_BOOKING"], procat["ORTHO"], procat["SURGEON"], procat["THERAPY"], procat["WHITE"], procat["PROSTHET"], procat["IMPLANT"]])
		f.seek(0)
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=eventorders_%s.csv' % datetime.date.today().strftime('%Y%m%d')
		return response
	export_medprocs.short_description = "Export Medprocs"
admin.site.register(MedProc, MedProcAdmin)