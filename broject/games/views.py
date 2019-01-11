from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Category, Game

def index(request):
    all_categories = Category.objects.all()

    return render(request, 'games/index.html',{'all_categories': all_categories})

def categoryView(request, category_id):
    #return HttpResponse("<h1>Single category view for caregory #" + str(category_id) + "</h1>")
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'games/categoryView.html',{'category': category})
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
