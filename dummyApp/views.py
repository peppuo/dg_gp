from django.shortcuts import render
from .forms import UserForm
from .models import User, Log


def render_template(request, pk=1):
    user = User.objects.get(pk=pk)
    form = UserForm(instance=user)
    return render(request, 'dummyApp/practice_form_template.html',
                  {'userform': form, 'user': user})


def render_logs(request):
    logs = Log.objects.all()
    return render(request, 'dummyApp/practice_template.html', {'logs': logs})


def render_base(request):
    return render(request, 'dummyApp/base.html')
