from django.shortcuts import render


def render_base(request):
    return render(request, 'base.html')


def render_tasks_table(request):
    return render(request, 'tryMaterialize/templates/tasks_table.html')
