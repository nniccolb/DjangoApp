from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Category, Game
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()

class DetailView(generic.DetailView):
    model = Category
    pk_url_kwarg='category_pk'
    template_name = 'games/categoryView.html'
class GameView(generic.DetailView):
    model = Game
    pk_url_kwarg='game_pk'
    template_name = 'games/gameView.html'
class GameCreate(CreateView):
    model = Game
    fields = ['category', 'price', 'title', 'source']
