from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import RecipeModel
from django.urls import reverse_lazy

# Create your views here.

class RecipeList(ListView):
    template_name = 'list.html'
    model = RecipeModel

class RecipeDetail(DetailView):
    template_name = 'detail.html'
    model = RecipeModel

class RecipeCreate(CreateView):
    template_name = 'create.html'
    model = RecipeModel
    fields = ('name','ingredients','process','category')
    success_url = reverse_lazy('list')

class RecipeDelete(DeleteView):
    template_name = 'delete.html'
    model = RecipeModel
    success_url = reverse_lazy('list')

class RecipeUpdate(UpdateView):
    template_name = 'update.html'
    model = RecipeModel
    success_url = reverse_lazy('list')
    fields = ('name','ingredients','process','category')

