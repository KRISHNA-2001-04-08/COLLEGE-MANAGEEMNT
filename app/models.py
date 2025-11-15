from django.db import models
from django.contrib.auth.models import AbstractUser


class Staff(AbstractUser):
    department=models.CharField(max_length=20)
    year=models.CharField(max_length=20)

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Rollnumber=models.CharField(max_length=100)
    DOB=models.DateField()
    Father=models.CharField(max_length=100)
    Mother=models.CharField(max_length=100)
    Occupation=models.CharField(max_length=100)
    Phoneno=models.CharField(max_length=10)
    Bloodgroup=models.CharField(max_length=10)
    DoorNo=models.CharField(max_length=100)
    Street=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    Pincode=models.CharField(max_length=6)
