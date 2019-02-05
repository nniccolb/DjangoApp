from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.CharField(max_length=100)
    games = models.ManyToManyField('Game')
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.userType

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

class Game(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
    highscore = models.PositiveIntegerField(default=0)
    
    image = models.CharField(max_length=500)
    developer = models.ForeignKey('UserProfile', on_delete=models.PROTECT, default=1)


    def get_absolute_url(self):
        return reverse('games:index')

    def __str__(self):
        return self.title
