from django.db import models


# Create your models here.

class Register(models.Model):
    uname = models.CharField(max_length=16)
    upwd = models.CharField(max_length=65)
