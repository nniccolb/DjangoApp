
from django.urls import path, include
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls'), {'template_name': 'games/login.html'}),
    path('register/', views.Registration.as_view(), name='registration'),
    path('profile/', views.profile, name='profile'),
    #path('login/', views.login, name='login'),
    path('<int:category_pk>/', views.DetailView.as_view(), name='categoryView'),
    path('<int:category_pk>/<int:game_pk>/', views.GameView.as_view(), name='gameView'),
    path('<int:category_pk>/<int:game_pk>/buy/', views.checksum, name='gameView'),
    path('add/', views.GameCreate.as_view(), name='game-add'),
    path('<int:category_pk>/<int:game_id>/success/',views.success_payment,name='payment_success'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('register/<uidb64>/<token>/', views.activate, name='activate'),
    path('save/', views.save, name='save') 
]
