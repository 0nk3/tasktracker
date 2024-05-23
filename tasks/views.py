from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(title=title, description=description)
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_new.html')

def task_edit(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_edit.html', {'task': task})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return render(request, 'tasks/task_delete.html')

def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

def task_delete_completed(request):
    Task.objects.filter(completed=True).delete()
    return render(request, 'tasks/task_delete_completed.html')

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')