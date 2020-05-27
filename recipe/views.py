from django.shortcuts import render
from django.views.generic import ListView
from .models import RecipeModel

# Create your views here.

class RecipeList(ListView):
    template_name = 'list.html'
    model = RecipeModel