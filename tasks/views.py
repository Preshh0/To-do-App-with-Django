from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

# def index(request):
#     return HttpResponse('Hello World')
def index(request):
    tasks = Task.objects.all()

    forms = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form':forms}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk): #pk = Primary Key
    task = Task.objects.get(id=pk)

    return render(request, 'task/update_task.html')