from modeltranslation.translator import translator, TranslationOptions
from .models import *

class MedProcTranslationOptions(TranslationOptions):
    pass #fields = ('title', 'title_check', 'description')

translator.register(MedProc, MedProcTranslationOptions)
#https://django-modeltranslation.readthedocs.io/en/latest/registration.html