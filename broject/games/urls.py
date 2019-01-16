
from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='loginView'),
    path('<pk>/', views.DetailView.as_view(), name='categoryView'),
    path('/add/', views.GameCreate.as_view(), name='game-add'),#Muuta tää kun saadaan view peleille
]
