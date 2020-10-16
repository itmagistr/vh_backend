from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import *
# Register your models here.
admin.site.register(MedProc, TranslationAdmin)