from django import forms
from .models import Eshop

class EshopForm(forms.ModelForm):
    class Meta:
        model = Eshop
        fields = '__all__'