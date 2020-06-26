from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from menu.models import Drink, Coffee, Bubbletea


class DrinkListView(ListView):
    model = Drink
    # paginate_by = 3


class CoffeeCreateView(CreateView):
    model = Coffee
    fields = '__all__'  #['category', 'name', 'price', 'image']
    template_name = 'drink_create.html'
    success_url = reverse_lazy('menu:list')

class BubbleteaCreateView(CreateView):
    model = Bubbletea
    fields = '__all__'  #['category', 'name', 'price', 'image']
    template_name = 'drink_create.html'
    success_url = reverse_lazy('menu:list')

class DrinkUpdateView(UpdateView):
    model = Drink
    fields = '__all__'  #['category', 'name', 'price', 'image']
    template_name_suffix = '_update'    #bookmark_update.html
    success_url = reverse_lazy('menu:list')

class DrinkDeleteView(DeleteView):
    model = Drink
    success_url = reverse_lazy('menu:list')