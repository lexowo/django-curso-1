from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def hello(request, username): #Recibe parametro de django (request) /espera parametro despues de slash
    return HttpResponse("<h1>Hola amigo %s.</h1>" %username) #poner param en el titulo

def about(request):
    return HttpResponse("About")