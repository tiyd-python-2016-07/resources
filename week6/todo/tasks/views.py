from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def example(request):
    print('=' * 20)
    print('GET:')
    print(request.GET)
    print('=' * 20)
    print('POST:')
    print(request.POST)
    print('=' * 20)
    return render(request, 'tasks/example.html')






def index(request):
    if request.POST:
        is_delete = 'delete' in request.POST

        if is_delete:
            task_id = int(request.POST['id'])
            task = Task.objects.get(id=task_id)
            task.delete()

        else:
            description = request.POST['description']
            status = int(request.POST['status'])

            if 'id' in request.POST:
                task_id = int(request.POST['id'])
                created = request.POST['created']
            else:
                task_id = None
                created = None

            t = Task(id=task_id, description=description, status=status, created=created)
            t.save()

    tasks = Task.objects.all().order_by('-status', '-updated')
    context = {
        'tasks': tasks,
        'statuses': Task.STATUSES.items(),
    }

    return render(request, 'tasks/index.html', context)
