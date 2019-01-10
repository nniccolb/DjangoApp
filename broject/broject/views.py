from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>nick on hieno ihminen :)</h1>")
