from modeltranslation.translator import translator, TranslationOptions
from .models import *

class RatingTranslationOptions(TranslationOptions):
     fields = ('title', 'description')

translator.register(Rating, RatingTranslationOptions)

# #https://django-modeltranslation.readthedocs.io/en/latest/registration.html