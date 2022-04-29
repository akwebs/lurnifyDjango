from django import forms
from .models import *




class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Phone Number",
                "class": "form-control"
            }
        ))
   