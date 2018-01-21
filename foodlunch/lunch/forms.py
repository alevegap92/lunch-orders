from django.forms import ModelForm
from django import forms
from .models import *
from django.forms import CheckboxSelectMultiple
class FoodTypeForm(ModelForm):
    class Meta:
        model = FoodType
        fields = '__all__'
        exclude = ['created','to_update']
        
    def __init__(self, *args, **kwargs):
        super(FoodTypeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })      

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        widgets = {
        'menu_name': forms.TextInput(attrs={'class':'form-control'}),
        'menu_foodtype': forms.CheckboxSelectMultiple,
        'price': forms.NumberInput(attrs={'class':'form-control'}),
        }    
        exclude = ['menu_time','created','to_update']

class OrderMenuForm(ModelForm):
    class Meta:
        model = OrderMenu
        exclude = ['ordertime','oderdate']

    def __init__(self, *args, **kwargs):
        super(OrderMenuForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })            
