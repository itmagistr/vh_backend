from modeltranslation.translator import translator, TranslationOptions
from .models import *

class CategoryTranslationOptions(TranslationOptions):
     fields = ('title', 'title_short', 'description')


translator.register(Category, CategoryTranslationOptions)

# #https://django-modeltranslation.readthedocs.io/en/latest/registration.html