from modeltranslation.translator import translator, TranslationOptions
from .models import *


translator.register(Client, TranslationOptions)
# #https://django-modeltranslation.readthedocs.io/en/latest/registration.html