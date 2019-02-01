from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.CharField(max_length=100)
    games = models.ManyToManyField('Game')

    def __str__(self):
        return self.userType

class Game(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
    
    image = models.CharField(max_length=500)
    developer = models.ForeignKey(UserProfile, on_delete=models.PROTECT)



    developer = models.ForeignKey('UserProfile',on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('games:index')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.CharField(max_length=100)
    games = models.ManyToManyField(Game)


    def __str__(self):
        return self.userType
