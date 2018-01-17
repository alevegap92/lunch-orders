from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *
# Create your views here.
#---------START VIEWS Menu--------------------#
class ListMenu(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menu'

class CreateMenu(CreateView):
    model = Menu
    template_name = 'food_form.html'
    form_class = MenuForm
    success_url = reverse_lazy('lunch:list_menu')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UpdateMenu(UpdateView):
    model = Menu
    template_name = 'food_form.html'
    form_class = MenuForm
    success_url = reverse_lazy('lunch:list_menu')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class DetailMenu(DetailView):
    model = Menu
    template_name = 'menu_detail.html'

class DeleteMenu(DeleteView):
    model = Menu
    template_name = 'food_delete.html'
    success_url = reverse_lazy('lunch:list_menu')

#---------END VIEWS Menu----------------------#
#---------START VIEWS FoodType ---------------#
class ListFoodType(ListView):
    model = FoodType
    template_name = 'food_list.html'
    context_object_name = 'foodtypes'

    def get_context_data(self, **kwargs):
        context = super(ListFoodType, self).get_context_data(**kwargs)           
        context['food_all'] = FoodType.objects.all()
        context['maindich'] = FoodType.objects.filter(foodselect='m')
        context['salad'] = FoodType.objects.filter(foodselect='s')
        context['dessert'] = FoodType.objects.filter(foodselect='d')
        return context

class CreateFoodType(CreateView):
    model = FoodType
    template_name = 'food_form.html'
    form_class = FoodTypeForm
    success_url = reverse_lazy('lunch:list_foodtype')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UpdateFoodType(UpdateView):
    model = FoodType
    template_name = 'food_form.html'
    form_class = FoodTypeForm
    success_url = reverse_lazy('lunch:list_foodtype')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class DetailFoodType(DetailView):
    model = FoodType
    template_name = 'food_detail.html'

class DeleteFoodType(DeleteView):
    model = FoodType
    template_name = 'food_delete.html'
    success_url = reverse_lazy('lunch:list_foodtype')

#---------END VIEWS FoodType -----------------#

