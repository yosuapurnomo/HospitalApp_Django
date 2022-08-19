from django.urls import path, re_path
from .views import RegistrationUser, login, logout

app_name = "user"
urlpatterns = [
    path('', login.as_view(), name='login'),
    path('registrationPasien', RegistrationUser.as_view(), name='regisPasien'),
    path('logout', logout.as_view(), name='logout')
]