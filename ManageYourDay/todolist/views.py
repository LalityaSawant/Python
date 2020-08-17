from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import ToDolist,MangedDay
from .generic_functions import get_priorities,create_no_task_day
import datetime

# Create your views here.

def viewManagedDay(request):
    ordered_data = ToDolist.objects.order_by('task_start_time')
    return render(request,'todolist.html',{'all_items': ordered_data})


def todolistView(request):
    all_todo_tasks = ToDolist.objects.all()
    return render(request,'todolist.html',{'all_items': all_todo_tasks})


def addTodo(request):
    #retrive required data from the list
    added_datetime = request.POST['starttime']
    if added_datetime == '':
        added_datetime = None
    added_content = request.POST['content']
    added_status = request.POST['status']
    added_category = request.POST['category']
    added_priority = get_priorities(added_category)

    #create new todoitem
    new_item = ToDolist(task_start_time=added_datetime,content = added_content, status = added_status, category = added_category, priority= added_priority)

    #save
    new_item.save()

    #redirect to user browser came from
    return HttpResponseRedirect('/todolist/')


def deleteTodo(request,todo_id):
    to_delete = ToDolist.objects.get(id=todo_id)
    to_delete.delete()
    #redirect to user browser came from
    return HttpResponseRedirect('/todolist/')


def vieweditTodo(request,todo_id):
    single_todo_tasks = ToDolist.objects.get(id=todo_id)
    return render(request,'edit.html',{'item': single_todo_tasks})


def updateToDo(request,todo_id):
    all_todo_tasks = ToDolist.objects.get(id=todo_id)
    all_todo_tasks.content = request.POST['content']
    all_todo_tasks.status = request.POST['status']
    all_todo_tasks.category = request.POST['category']
    all_todo_tasks.save()
    return HttpResponseRedirect('/todolist/')


def myToDoHome(request):
    #create_no_task_day()
    all_todo_tasks = MangedDay.objects.order_by('task_start_time')#all()
    return render(request,'home.html',{'all_items': all_todo_tasks})
