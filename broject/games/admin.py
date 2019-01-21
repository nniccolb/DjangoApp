from django.contrib import admin
from .models import Category, Game, UserProfile

admin.site.register(Category)
admin.site.register(Game)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'userType']
admin.site.register(UserProfile, UserProfileAdmin )
