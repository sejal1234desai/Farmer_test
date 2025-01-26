# forms.py
from django import forms
from .models import Farmer, TreeSpecies, ImplementationDetail

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'contact', 'field_photo', 'plot_location']

class TreeSpeciesForm(forms.ModelForm):
    class Meta:
        model = TreeSpecies
        fields = ['species_name', 'quantity']

class ImplementationDetailForm(forms.ModelForm):
    class Meta:
        model = ImplementationDetail
        fields = ['farmer', 'notes']
