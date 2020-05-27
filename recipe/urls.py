from django.urls import path
from .views import RecipeList

urlpatterns = [
    path('list/', RecipeList.as_view())
]
