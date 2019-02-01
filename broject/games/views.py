from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Game, UserProfile
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.views.generic import View
from .forms import UserForm
from hashlib import md5


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
    fields = ['category', 'price', 'title', 'source', 'image']

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
            usertype = form.cleaned_data['user_type']
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, userType=usertype)
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('games:index')

        return render(request, self.template_name, {'form': form})


def checksum(request, game_pk,category_pk):
    game = Game.objects.get(id=game_pk)
    pid = request.user.id
    sid = 'broject112'
    amount = game.price
    secret_key = 'ec5ed80e615f3d4739e689d6e24b4b81'
    unhashed = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(unhashed.encode("ascii"))
    checksum = m.hexdigest()
    context = {
			'pid': pid,
			'sid': sid,
			'amount': amount,
			'secret_key': secret_key,
			'checksum': checksum,
			'game_id': game_pk,
			'game': game,

    }

	# sending context to payment-template
    return render(request, 'games/gameView.html', context)

def success_payment(request,game_id,category_pk):
    pid = request.GET['pid']
    ref = request.GET['ref']

    url_checksum = request.GET['checksum']

    secret_key = "5ba99a03e46a687041b16ec552bcdf9c"

    checksum_str = "pid={}&ref={}&result={}&token={}".format(pid, ref, "success", secret_key)

    m = md5(checksum_str.encode("ascii"))
    checksum = m.hexdigest()

    #buyer_id = pid.split('-')[0]
    #game_id = pid.split('-')[1]
    game = Game.objects.get(id=game_id)
    category = game.category

    current_user = request.user

    context = {
	    'game': game,
        'category': category,

    }

    if request.user.is_authenticated:
	    if url_checksum == checksum and str(current_user.id) == user_id and str(game_id) == gameid:
            

		    user = UserProfiles.objects.get(id=current_user.id)



    return render(request, 'games/payment_success.html', context)
