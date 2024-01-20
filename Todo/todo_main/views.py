from django.shortcuts import render
from todo.models import Task

def home(request):
    undone_tasks = Task.objects.filter(is_completed = False).order_by('updated_at')
    done_tasks = Task.objects.filter(is_completed = True)
    context = {
        "undone": undone_tasks,
        "done": done_tasks,
    }
    return render(request, 'home.html', context)