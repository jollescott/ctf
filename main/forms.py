from django import forms

from .fields import SECRET_LENGTH

class EnterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)

class SecretForm(forms.Form):
    secret = forms.CharField(label='Secret', max_length=SECRET_LENGTH)