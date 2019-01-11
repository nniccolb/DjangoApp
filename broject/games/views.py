from django.http import Http404
from django.shortcuts import render
from .models import Category

def index(request):
    all_categories = Category.objects.all()

    return render(request, 'games/index.html',{'all_categories': all_categories})

def categoryView(request, category_id):
    #return HttpResponse("<h1>Single category view for caregory #" + str(category_id) + "</h1>")
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("category not exist")
    return render(request, 'games/categoryView.html',{'category': category})
