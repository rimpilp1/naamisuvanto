from django import forms
from .models import Saalis
import datetime
from django.conf import settings

class SaalisForm(forms.ModelForm):
	#"saantipaiva" = forms.DateField(widget=SelectDateWidget(), initial=yesterday)
	
	class Meta:
		model = Saalis
		fields = [
        "saaja",
		"paikka",
		"paino",
		"pituus",
        "viehe",
		"email",
        "saantipaiva",
		"kuva",
		"public",
		"sukupuoli",
		]
		labels = {
			"email": "Sähköposti",
		}
		widgets = {
			'saantipaiva': forms.SelectDateWidget(),
		}

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)