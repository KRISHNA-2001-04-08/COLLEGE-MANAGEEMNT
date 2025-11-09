from django.db import models
from django.contrib.auth.models import AbstractUser


class Staff(AbstractUser):
    department=models.CharField(max_length=20)
    year=models.CharField(max_length=20)

# Create your models here.
