from django.shortcuts import render, redirect
from tasks.forms import NewTaskForm
from tasks.models import Task
from django.utils import timezone


def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Task.objects.create(name=cd['new_name'], frequency=cd['new_rate'])
            return redirect('/')
        return redirect('/')
    if request.method == 'GET':
        overdue = []
        upcoming = []
        completed = []
        for task in Task.objects.all():
            if task.time_remaining() >= 10:
                completed.append(task)
            elif task.time_remaining() < 0:
                overdue.append(task)
            else:
                upcoming.append(task)
        return render(request, 'homepage.html', {'form': NewTaskForm(), 'overdue': overdue, 'upcoming': upcoming, 'completed': completed})


def delete(request):
    if request.method == 'GET':
        try:
            # Get desired patient id from url
            task = Task.objects.get(id=request.GET.get('id'))
            task.delete()
            return redirect('/')
        except Task.DoesNotExist:
            return redirect('/')


def update(request):
    try:
        # Get desired patient id from url
        task = Task.objects.get(id=request.GET.get('id'))
        task.complete()
        return redirect('/')
    except Task.DoesNotExist:
        return redirect('/')
