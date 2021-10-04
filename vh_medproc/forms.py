from django import forms
from django.forms.widgets import TextInput
from .models import MedProc

class MedProcAdminForm(forms.ModelForm):
	class Meta:
		exclude = []
		model = MedProc
		widgets = {
			'title_check_ru': TextInput(attrs={'size':'200'}), 
			'title_check_en': TextInput(attrs={'size':'200'}), 
			'title_ru': TextInput(attrs={'size':'200'}), 
			'title_en': TextInput(attrs={'size':'200'}), 
		}
