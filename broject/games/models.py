from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Game(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creator = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
