from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Game
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.views.generic import View
from .forms import UserForm


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

class Registration(View):
    form_class = UserForm
    template_name = 'games/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('games:index')

        return render(request, self.template_name, {'form': form})
