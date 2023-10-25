from django.db import models

# Create your models here.

class User(models.Model):
    uname =models.CharField(max_length=20)
    uloc  =models.CharField(max_length=20)

