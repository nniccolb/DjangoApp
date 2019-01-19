
from django.urls import path, include
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls'), {'template_name': 'games/login.html'}),
    path('register/', views.Registration.as_view(), name='registration'),
    #path('login/', views.login, name='login'),
    path('<int:category_pk>/', views.DetailView.as_view(), name='categoryView'),
    path('<int:category_pk>/<int:game_pk>/', views.GameView.as_view(), name='gameView'),
    path('add/', views.GameCreate.as_view(), name='game-add'),
]
