from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
	title='Django Course!!'
	return render(request, 'index.html', {
		'tittle': title #pasar la variable al html no tiene que ser el mismo nombre
	})

def about(request):
	username='tron' #todo lo convierte a string
	return render(request, 'about.html', {
		'username':username
	})

def hello(request, username): #Recibe parametro de django (request) /espera parametro despues de slash
	return HttpResponse("<h1>Hola amigo %s.</h1>" %username) #poner param en el titulo

def projects(request):
	#projects=list(Project.objects.values())
	projects=Project.objects.all() #se pueden pasar datos de la base de datos pero asi solo los convierte en strings directos
	return render(request,'projects.html', {
		'projects':projects
	})

def tasks(request):
	#task=get_object_or_404(Task, id=id)
	tasks = Task.objects.all()
	return render(request,'tasks.html', {
		'tasks': tasks
	})

def create_task(request):
	if request.method == 'GET':
		# print(request.GET['title'])
		# print(request.GET['description'])
		return render(request, 'create_task.html', {
			'form': CreateNewTask()
		})
	else:
		Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
		return redirect('/tasks/')