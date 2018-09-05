from django.db import models
import datetime
# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='名字')
    address = models.CharField(max_length=50)
    website = models.URLField()


class AuthorManager(models.Manager):
    def lessThan(self, count):
        return self.filter(age__lt=count)


class Author(models.Model):
    objects = AuthorManager()
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    picture = models.ImageField(null=True, upload_to='static/upload/usring')
    publisher = models.ManyToManyField(Publisher, null=True)

    def __str__(self):
        return str(self.id) + "  " + self.name


class Wife(models.Model):
    name = models.CharField(max_length=20)
    author = models.OneToOneField(Author)


class Book(models.Model):
    title = models.CharField(max_length=20)
    Publisher = models.DateTimeField(default=datetime.datetime.now())
