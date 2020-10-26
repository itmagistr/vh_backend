from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


admin.site.register(Doctor, admin.ModelAdmin)
admin.site.register(Special, TranslationAdmin)
admin.site.register(Level, TranslationAdmin)