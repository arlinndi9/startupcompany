from django import forms
from startupcompany.models import apply_job,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    firstname=forms.CharField(max_length=50,required=True)
    lastname=forms.CharField(max_length=50,required=True)
    email=forms.EmailField(max_length=100,required=True)
    comment = forms.CharField(widget=forms.Textarea)

class apply_job(forms.ModelForm):
    class Meta:
        model=apply_job
        fields='__all__'

class Contact(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"

