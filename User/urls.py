from django.urls import path, re_path
from .views import RegistrationUser

app_name = 'user'
urlpatterns = [
    path('registrationPasien', RegistrationUser.as_view(), name='regisPasien')
]