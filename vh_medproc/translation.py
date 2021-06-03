from modeltranslation.translator import translator, TranslationOptions
from .models import *

class MedProcTranslationOptions(TranslationOptions):
    fields = ('recomend_before', 'recomend_after')

translator.register(MedProc, MedProcTranslationOptions)
#https://django-modeltranslation.readthedocs.io/en/latest/registration.html