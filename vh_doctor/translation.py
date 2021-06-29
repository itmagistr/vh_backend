from modeltranslation.translator import translator, TranslationOptions
from .models import *

class SpecialTranslationOptions(TranslationOptions):
     fields = ('title', 'description')

class LevelTranslationOptions(TranslationOptions):
     fields = ('title', 'description')

class DegreeTranslationOptions(TranslationOptions):
     fields = ('title', 'description')

class DoctorTranslationOptions(TranslationOptions):
     fields = ('сertificate', 'education')
     
translator.register(Special, SpecialTranslationOptions)
translator.register(Level, LevelTranslationOptions)
translator.register(Doctor, DoctorTranslationOptions)
translator.register(Degree, DegreeTranslationOptions)

# #https://django-modeltranslation.readthedocs.io/en/latest/registration.html