from django import forms
from .models import *

class Userform(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields='__all__'