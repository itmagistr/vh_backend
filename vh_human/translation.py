from modeltranslation.translator import translator, TranslationOptions
from .models import *

class HumanTranslationOptions(TranslationOptions):
    fields = ('firstName', 'lastName', 'midName')

translator.register(Human, HumanTranslationOptions)
#https://django-modeltranslation.readthedocs.io/en/latest/registration.html