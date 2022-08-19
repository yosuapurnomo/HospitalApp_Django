from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .models import User
from .forms import UserForm, authentication


# Create your views here.
class RegistrationUser(CreateView):
    model = User
    template_name = 'user/registration.html'
    success_url = reverse_lazy('user:login')
    form_class = UserForm
    extra_context = {
        'title': "Registration Pasien"
    }

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)


class login(SuccessMessageMixin, LoginView):
    authentication_form = authentication
    template_name = 'user/login.html'
    query_string = True
    success_message = "Success Login"

    def get(self, request, *args, **kwargs):
        print(request.user)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        self.success_url = reverse_lazy('user:regisPasien')
        return self.success_url

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"message":"Something wrong"})
        return self.render_to_response(context)

class logout(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('user:login')
    success_message = "Success Logout"
