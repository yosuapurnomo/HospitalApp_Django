from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'username':forms.TextInput(attrs={
                'class':'form-control',
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password1']
        del self.fields['password2']