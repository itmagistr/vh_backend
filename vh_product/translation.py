from modeltranslation.translator import translator, TranslationOptions
from .models import *

class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'title_check', 'description')

translator.register(Product, ProductTranslationOptions)
#https://django-modeltranslation.readthedocs.io/en/latest/registration.html