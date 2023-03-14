from django import forms
from .models import Customer, Vehicle

class CustomerForm(forms.ModelForm):
    class Meta: 
        model = Customer
        fields = ('__all__')


class VehicleForm(forms.ModelForm):
    class Meta: 
        model = Vehicle
        fields = ('__all__')