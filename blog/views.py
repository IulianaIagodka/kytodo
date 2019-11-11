from django.shortcuts import render
from models import Todo
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    if request.method == 'POST':
        title = request.POST['title']
        todo = Todo(title=title)
        todo.save()
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',context)

def show_completed(request): #show completed task only
    todos = Todo.objects.filter(completed=True)
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def show_active(request):   #show active task list
    todos = Todo.objects.filter(completed=False)
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)
def clear_completed(request):    #Delete the completed tasks
    Todo.objects.filter(completed=True).delete()
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def save_state(request):
     pass
