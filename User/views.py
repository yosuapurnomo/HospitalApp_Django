from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import UserForm


# Create your views here.
class RegistrationUser(CreateView):
    model = User
    template_name = 'user/registration.html'
    form_class = UserForm
    extra_context ={
        'title':"Registration Pasien"
    }
