from django.http import HttpResponse

# Create your views here.
def hello(request): #Recibe parametro de django (request)
    return HttpResponse("<h1>Hola amigo.</h1>")

def about(request):
    return HttpResponse("About")