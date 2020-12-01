from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class DoctorAdmin(TranslationAdmin):
	model = Doctor
	readonly_fields=('uid',)
	list_display = ('human_fio', 'level', 'degree', 'rating')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Special, TranslationAdmin)
admin.site.register(Level, TranslationAdmin)
admin.site.register(Degree, TranslationAdmin)