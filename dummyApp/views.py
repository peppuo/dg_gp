from django.shortcuts import render
from .forms import UserForm, LogForm
from .models import User, Log


def render_base(request):
    return render(request, 'dummyApp/base.html')


def render_logs(request):
    logs = Log.objects.all()
    return render(request, 'dummyApp/logs_template.html', {'logs': logs})


def render_insert_log(request):
    log = Log
    log_form = LogForm(instance=log)
    return render(request, 'dummyApp/insert_log.html',
                  {'log': log, 'log_form': log_form})


def render_edit_user(request, pk=1):
    user = User.objects.get(pk=pk)
    form = UserForm(instance=user)
    return render(request, 'dummyApp/edit_user.html',
                  {'user': user, 'user_form': form})
