from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from vh_product.models import ProductEmployee
from vh_doctor.models import DocWorkRes
# Register your models here.

class DocWorkResInline(admin.TabularInline):
	model = DocWorkRes
	extra = 1

class EmployeeProdInline(admin.TabularInline):
	model = ProductEmployee
	extra = 1

class DoctorAdmin(TranslationAdmin):
	model = Doctor
	readonly_fields=('uid',)
	list_display = ('human_fio', 'level', 'degree', 'rating')
	inlines = [DocWorkResInline, EmployeeProdInline]

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Special, TranslationAdmin)
admin.site.register(Level, TranslationAdmin)
admin.site.register(Degree, TranslationAdmin)