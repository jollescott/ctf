from django import forms

class EnterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)