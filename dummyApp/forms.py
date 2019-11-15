from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email_address', 'department', )
        labels = {'first_name': 'First Name', 'last_name': 'Last Name',
                  'email_address': 'Email Address', 'department': 'Department',
                  }
