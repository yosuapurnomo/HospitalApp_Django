from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin


# Create your models here.
class Provincies(models.Model):
    name = models.CharField(max_length=50)


class cities(models.Model):
    provinceId = models.ForeignKey('Provincies', related_name='province', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class User(AbstractUser):
    name = models.CharField(max_length=15)
    username = models.CharField(verbose_name="Username", max_length=25, unique=True)
    email = models.EmailField(verbose_name="Email address", unique=True, blank=False)
    emailVerifiedAt = models.DateTimeField(name="Email Verrified At")
    nik = models.CharField(max_length=16, null=True, blank=True)
    dateOfBirth = models.DateField(name="Birthday", null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    provinceId = models.ForeignKey('Provincies', null=True, blank=True, related_name='provincies',
                                   on_delete=models.CASCADE)
    city = models.ForeignKey('cities', null=True, blank=True, related_name='cities', on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    type = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(3)])
    first_name = None
    last_name = None
