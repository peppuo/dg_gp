from django.shortcuts import render, reverse, redirect
from .forms import UserForm, LogForm
from .models import User, Log


def render_base(request):
    return render(request, 'dummyApp/base.html')


def get_logs(request):
    logs = Log.objects.all()
    return render(request, 'dummyApp/logs_template.html', {'logs': logs, })


def insert_log(request):
    if request.method == 'POST':
        filled_form = LogForm(request.POST)
        print('\n\nfilled_form:', filled_form)
        check_constrain = filled_form.cleaned_data['started'] < filled_form.cleaned_data['finished']
        print('\n\ncheck_constrain:', check_constrain)
        if filled_form.is_valid() and check_constrain:
            filled_form.save()
            return redirect(reverse('get_logs'))
        elif not check_constrain:
            note = 'Log not inserted. The start time is after the finish time!'
        else:
            note = 'Log not inserted, please review details!'
        return render(request, 'dummyApp/insert_log.html',
                      {'form': filled_form, 'note': note})
    form = LogForm()
    return render(request, 'dummyApp/insert_log.html',
                  {'form': form})


def edit_log(request, pk):
    log = Log.objects.get(pk=pk)
    form = LogForm(instance=log)
    if request.method == 'POST':
        filled_form = LogForm(request.POST, instance=log)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Your log has been edited'
            logs = Log.objects.all()
            return render(request, 'dummyApp/logs_template.html',
                          {'note': note, 'logs': logs})
        else:
            note = 'The order was not created, please review details'
            render(request, 'dummyApp/edit_log.html',
                   {'log': log, 'form': filled_form, 'note': note})
    return render(request, 'dummyApp/edit_log.html',
                  {'log': log, 'form': form})


def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    form = UserForm(instance=user)
    return render(request, 'dummyApp/edit_user.html',
                  {'user': user, 'form': form})
