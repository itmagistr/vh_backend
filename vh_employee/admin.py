from django.contrib import admin
from .models import *
#from modeltranslation.admin import TranslationAdmin


class EmployeeAdmin(admin.ModelAdmin):
	model = Employee

admin.site.register(Employee, EmployeeAdmin)

class EmpRoleAdmin(admin.ModelAdmin):
	model = EmpRole

admin.site.register(EmpRole, EmployeeAdmin)