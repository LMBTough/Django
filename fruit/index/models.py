from django.db import models
import datetime
# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=20)
    Publisher = models.DateTimeField(default=datetime.datetime.now())
