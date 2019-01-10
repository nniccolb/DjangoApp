from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Frontpage (Nic on hieno ihminen :))</h1>")
