from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()

class User(models.Model):
    uname=models.CharField(max_length=32)
    uemail=models.CharField(max_length=32)