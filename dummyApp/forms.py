from django import forms
from .models import User


class FormPractice(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email_address', 'department',
                  'registered', )
