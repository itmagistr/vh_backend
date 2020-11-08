from django.contrib import admin
from .models import *

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
	model = Booking
	readonly_fields=('uid',)

class TimeSlotAdmin(admin.ModelAdmin):
	model = TimeSlot
	readonly_fields=('uid',)

admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Booking, BookingAdmin)