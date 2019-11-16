from django import forms
from .models import User, Log


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email_address', 'department', )
        labels = {'first_name': 'First Name', 'last_name': 'Last Name',
                  'email_address': 'Email Address', 'department': 'Department',
                  }


class LogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ('task', 'user', 'status', 'started', 'finished')
        labels = {'task': 'Task', 'user': 'Email Address', 'status': 'Status',
                  'started': 'Started', 'finished': 'Finished', }

