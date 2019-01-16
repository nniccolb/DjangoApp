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
    template_name = 'games/categoryView.html'

def favorite(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    try:
        selected_game = category.game_set.get(pk=request.POST['game'])
    except (KeyError, Game.DoesNotExist):
        return render(request, 'games/categoryView.html', {
        'category': category,
        'error_message': "You did not select a valid game",
        })
    else:
        selected_game.favorite = True
        selected_game.save()
        return render(request, 'games/categoryView.html',{'category': category})

class GameCreate(CreateView):
    model = Game
    fields = ['category', 'price', 'title', 'source']