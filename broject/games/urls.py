
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.categoryView, name='categoryView'),
    path('<int:category_id>/favorite', views.favorite, name='favorite'),
]
