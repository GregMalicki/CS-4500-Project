from django.shortcuts import render, redirect
from tasks.forms import NewTaskForm
from tasks.models import Task


def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Task.objects.create(name=cd['new_name'], frequency=cd['new_rate'])
            return render(request, 'homepage.html', {'form': NewTaskForm(), 'tasks': Task.objects.all()})
        return render(request, 'homepage.html', {'form': NewTaskForm(), 'tasks': Task.objects.all()})
    if request.method == 'GET':
        return render(request, 'homepage.html', {'form': NewTaskForm(), 'tasks': Task.objects.all()})


def delete(request):
    if request.method == 'GET':
        try:
            # Get desired patient id from url
            task = Task.objects.get(id=request.GET.get('id'))
            task.delete()
            return redirect('/')
        except Task.DoesNotExist:
            return redirect('/')

