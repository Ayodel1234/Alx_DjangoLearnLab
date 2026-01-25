from django import forms
from .models import Resource


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ["name"]