from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def login_views(request):
    return render(request, 'login.html')


def add_author_views(request):
    Author.objects.create(name='王', age=33, email="947429662@qq.com")
    return HttpResponse('ADD OK!')


def add_book_views(request):
    Book.objects.create(title='红楼梦',
                        Publisher='1995-12-12')
    obj = Book(title='西游记',
               Publisher='1982-10-12')
    obj.save()
    return HttpResponse('Add Book Ok!')


def add_publisher_views(request):
    Publisher.objects.create(name='中国出版', address='五道口',
                             website='http://www.renmin.com')

    obj = Publisher(name='中国动画', address='五潘家园',
                    website='http://www.donghuapian.com')
    obj.save()
    return HttpResponse('Return OK!')


def get_author_views(request):
    authors = Author.objects.get(name="王")
    return render(request, 'show_authors.html', locals())


def get_author_list_views(request):
    authors = Author.objects.all()
    return render(request, 'show_author_list.html', locals())
