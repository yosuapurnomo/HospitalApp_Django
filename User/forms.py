from django import forms
from django.contrib.auth import password_validation

from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1']

        error_messages = {
            'username': {
                'unique': 'Your Custom Error Message here !!!',
            },
        }

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
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
            })
        }



class authentication(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password."
        ),
        'inactive': (
            "This Account is inactive"
        )
    }

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )