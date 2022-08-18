from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
	""" The model form for the website model """
	class Meta:
		model = Website