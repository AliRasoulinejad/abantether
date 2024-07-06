from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cellphone = models.CharField(max_length=13)

    class Meta:
        swappable = "AUTH_USER_MODEL"
