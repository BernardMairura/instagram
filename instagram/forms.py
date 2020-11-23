from django import forms
from .models import Image,Profile,Comment


class profileForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

