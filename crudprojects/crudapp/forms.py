from django import forms
from crudapp.models import Bike

class BikeForm(forms.ModelForm):
	class Meta:
		model=Bike
		fields='__all__'