from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def hello(request, username): #Recibe parametro de django (request) /espera parametro despues de slash
    return HttpResponse("<h1>Hola amigo %s.</h1>" %username) #poner param en el titulo

def about(request):
    return HttpResponse("About")

def projects(request):
    projects=list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    #task=get_object_or_404(Task, id=id)
    task=Task.objects.get(title=title)
    return HttpResponse('task: %s' % task.title)