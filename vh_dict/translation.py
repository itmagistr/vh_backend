from modeltranslation.translator import translator, TranslationOptions
from .models import *

class DictStringTranslationOptions(TranslationOptions):
    fields = ('title', 'title_short')

translator.register(DictString, DictStringTranslationOptions)
#https://django-modeltranslation.readthedocs.io/en/latest/registration.html