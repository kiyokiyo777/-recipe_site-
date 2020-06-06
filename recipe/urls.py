from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate, RecipeDelete, RecipeUpdate

urlpatterns = [
    path('list/', RecipeList.as_view(), name='list'),
    path('detail/<int:pk>', RecipeDetail.as_view(), name='detail'),
    path('create/', RecipeCreate.as_view(), name='create'),
    path('delete/<int:pk>', RecipeDelete.as_view(), name='delete'),
    path('update/<int:pk>', RecipeUpdate.as_view(), name='update'),
]
