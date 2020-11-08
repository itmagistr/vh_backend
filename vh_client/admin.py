from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class ClientAdmin(TranslationAdmin):
	model = Client
	readonly_fields=('uid',)

admin.site.register(Client, ClientAdmin)



#283bf485-22ea-436f-ad83-77a94fc33614