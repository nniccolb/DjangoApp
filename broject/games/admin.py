from django.contrib import admin
from .models import Category, Game, UserProfile, Score

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Score)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'userType']
admin.site.register(UserProfile, UserProfileAdmin)
