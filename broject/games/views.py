from django.http import HttpResponse
from django.template import loader
from .models import Category

def index(request):
    all_categories = Category.objects.all()
    template = loader.get_template('games/index.html')
    context = {
        'all_categories': all_categories
    }
    return HttpResponse(template.render(context, request))

def categoryView(request, category_id):
    return HttpResponse("<h1>Single category view for caregory #" + str(category_id) + "</h1>")
