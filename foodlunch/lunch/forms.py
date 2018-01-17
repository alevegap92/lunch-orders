from django.forms import ModelForm
from .models import *

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

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['created','to_update']

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class OrderMenuForm(ModelForm):
    class Meta:
        model = OrderMenu
        fields = '__all__'
        exclude = ['ordertime','oderdate']

    def __init__(self, *args, **kwargs):
        super(OrderMenuForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })            