from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>hey dude</h1>")

def singleView(request, game_id):
    return HttpResponse("<h1>Single game view for game #" + str(game_id) + "</h1>")
