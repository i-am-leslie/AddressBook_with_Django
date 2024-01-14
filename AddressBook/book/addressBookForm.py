from django.forms import ModelForm
from django import forms
from .models import AddressBook


class UploadForm(ModelForm):
    name=forms.CharField(max_length=255)
    class Meta:
        model = AddressBook
        fields = ['name']

