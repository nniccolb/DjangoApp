from django.http import HttpResponse

def index(request):
    return HttpResponse("Please make your way to the webstore <a href='games/'>here</a>")
