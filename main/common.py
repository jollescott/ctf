from main.models import Task


def get_base_context(request):
    tasks = Task.objects.all()
    module_tasks = dict(map(lambda t: (t.module, [t]), tasks))

    context = {"module_tasks": module_tasks, "user": request.user}
    return context
