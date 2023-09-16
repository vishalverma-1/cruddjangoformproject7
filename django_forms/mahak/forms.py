from django import forms
from django.forms import ModelForm
from . models import vivan



class studentform(forms.ModelForm):
    class Meta:
        model=vivan
        fields="__all__"