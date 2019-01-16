
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<pk>/', views.DetailView.as_view(), name='categoryView'),
    path('<pk>/add/', views.GameCreate.as_view(), name='game-add'),
    path('<int:category_id>/favorite', views.favorite, name='favorite'),
]
