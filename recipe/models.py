from django.db import models

class RecipeModel(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.TextField()
    process = models.TextField()
    category = models.CharField(max_length=20)
