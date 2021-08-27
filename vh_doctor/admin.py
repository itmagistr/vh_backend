from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from vh_product.models import ProductEmployee
from vh_doctor.models import DocWorkRes, DocCategory
from django.http import HttpResponse
import csv
from io import StringIO
import datetime
# Register your models here.

class DocWorkResInline(admin.TabularInline):
	model = DocWorkRes
	extra = 1

class EmployeeProdInline(admin.TabularInline):
	model = ProductEmployee
	extra = 1

class DocCategoryInline(admin.TabularInline):
	model = DocCategory
	extra = 1

class DoctorAdmin(TranslationAdmin):
	model = Doctor
	readonly_fields=('uid',)
	list_display = ('human_fio', 'uid', 'level', 'degree', 'rating')
	inlines = [DocCategoryInline, DocWorkResInline, EmployeeProdInline]

	actions = ["export_doctors", ]
	def export_doctors(self, request, queryset):
		f = StringIO()
		writer = csv.writer(f, delimiter=str(';'))
		writer.writerow(u'\ufeff')
		writer.writerow([u"doc_id", u"doc_uid", u"doc_special_code", u"doc_fname_ru", u"doc_lname_ru", u"doc_midname_ru", u"doc_fname_en", u"doc_lname_en", u"doc_midname_en", u"doc_phone",
						u"HYGIENIST", u"THERAPIST", u"ORTHOPEDIST", u"ORTHODONTIST", u"PERIODONTIST", u"SURGEON", u"IMPLANTOLOGIST"])
		for s in Doctor.objects.all():
			doccat = {"HYGIENIST": 0, "THERAPIST": 0, "ORTHOPEDIST": 0, "ORTHODONTIST": 0, "PERIODONTIST": 0, "SURGEON": 0, "IMPLANTOLOGIST": 0, }
			for dc in DocCategory.objects.filter(doctor=s):
				doccat[dc.category.code] = 1
			writer.writerow([s.id, s.uid, s.special.code, s.firstName_ru, s.lastName_ru, s.midName_ru, s.firstName_en, s.lastName_en, s.midName_en, s.phone, 
							doccat["HYGIENIST"], doccat["THERAPIST"], doccat["ORTHOPEDIST"], doccat["ORTHODONTIST"], doccat["PERIODONTIST"], doccat["SURGEON"], doccat["IMPLANTOLOGIST"]])
		f.seek(0)
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=doctors_%s.csv' % datetime.date.today().strftime('%Y%m%d')
		return response
	export_doctors.short_description = "Export Doctors"

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Special, TranslationAdmin)
admin.site.register(Level, TranslationAdmin)
admin.site.register(Degree, TranslationAdmin)