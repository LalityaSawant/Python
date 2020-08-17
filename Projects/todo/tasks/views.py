from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def home_view(request):
    return render(request, 'tasks/welcome.html')


def index(request):
    # return HttpResponse('Hello World!')
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks/list.html')

    context = {'tasks': tasks, 'form': form}

    return render(request, 'tasks/list.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    # form = TaskForm(instance=task)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'tasks/delete_task.html', context)


def review_task(request):
    # return HttpResponse('Hello World!')
    tasks = Task.objects.all()

    form = TaskForm()
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(request, 'tasks/review_task.html', context)
