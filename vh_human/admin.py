from django.contrib import admin
from .models import *
from vh_doctor.models import *

# Register your models here.
class DoctorInline(admin.TabularInline):
	model = Doctor
	extra = 0

class HumanAdmin(admin.ModelAdmin):
	model = Human
	inlines = [DoctorInline,]

admin.site.register(Human, HumanAdmin)