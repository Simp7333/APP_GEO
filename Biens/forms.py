from django.forms import ModelForm
from .models import *
from django import forms 


class formBiens(ModelForm):
  
    class Meta:
        model = Biens
        fields = [
            'nom', 'type', 'proprietaire', 'dimension', 'adresse','latitude','longitude','document','image'
        ]

        widgets = {
            'nom': forms.TextInput(
                attrs = {
                    'placeholder': 'Entrez le nom du Bien',
                    'class':'form-control'
                }
            ),

            'type': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            
            'proprietaire': forms.TextInput(
                attrs={
                    'placeholder': 'Entrez le nom de l\'auteur',
                    'class': 'form-control'
                }
            ),

            'dimension': forms.TextInput(
                attrs={
                    'placeholder': 'Entrez la dimension du bien',
                    'class': 'form-control'
                }
            ),

            'adresse': forms.TextInput(
                attrs={
                    'placeholder': 'Entrez le quartier du bien',
                    'class': 'form-control'
                }
            ),

            'document': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
           
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'longitude': forms.TextInput(
                attrs={
                    'class': 'form-control-file',
                    'type' : 'hidden'
                }
            ),

            'latitude': forms.TextInput(
                attrs={
                    'class': 'form-control-file',
                    'type' : 'hidden'
                }
            ),
        }
    def __init__(self, *args, **kwargs):
        super(formBiens, self).__init__(*args, **kwargs)
        self.fields['nom'].error_messages = {
            'required': 'Le nom du biens est obligatoire',
            'invalid': 'Veuillez entrer un nom correct.'
        }
        self.fields['type'].error_messages = {
            'required': 'La catégorie est obligatoire',
            'invalid': 'Veuillez sélectionner une catégorie valide'
        }
        self.fields['proprietaire'].error_messages = {
            'required': 'L\'auteur du biens est obligatoire',
            'invalid': 'Veuillez entrer un prix correct.'
        }
        self.fields['dimension'].error_messages = {
            'required': 'La dimention est obligatoire.',
            'invalid': 'Veuillez entrer une dimention valide.'
        }
        self.fields['adresse'].error_messages = {
            'required': 'La quartier est obligatoire.',
            'invalid': 'Veuillez entrer une quartier valide.'
        }
       
class formCat(ModelForm):
  
    class Meta:
        model = Categories
        fields = [
            'name'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder': 'Entrez le nom de la categorie',
                    'class':'form-control'
                }
            ),
        }
        
    def __init__(self, *args, **kwargs):
        super(formCat, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': 'Le nom du biens est obligatoire',
            'invalid': 'Veuillez entrer un nom correct.'
        }