from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def all(request):
    todos = Todo.objects.all()
    return render(request, 'todo/all.html', {"todos": todos})

def create(request):
    name = request.GET["name"]
    todo = Todo.objects.create(name=name)
    return redirect(all)

def delete(request, id):
    todo = Todo.objects.filter(id=id).delete()
    return redirect(all)