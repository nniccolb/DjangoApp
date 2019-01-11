from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Game(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
