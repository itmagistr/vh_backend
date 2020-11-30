from django.contrib import admin
from .models import *


class FeedbackAdmin(admin.ModelAdmin):
	model = Feedback
	readonly_fields = ['uid']
	list_display = ('fb_type', 'phone', 'email', 'name')

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FeedbackType, admin.ModelAdmin)
