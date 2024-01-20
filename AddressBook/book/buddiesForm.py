from django.forms import ModelForm
from django import forms
from .models import AddressBook
from .models import BuddyInfo

class UploadForm2(ModelForm):
    name=forms.CharField(max_length=255)
    Address=forms.CharField()
    Phone_Number=forms.IntegerField()
    Address_book=forms.ModelChoiceField(queryset=AddressBook.objects.all())
    class Meta:
        model = BuddyInfo
        fields = ['name','Address','Phone_Number','Address_book']