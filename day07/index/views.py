from django.shortcuts import render
from .models import *
# Create your views here.


def index_views(request):
    return render(request, 'index.html', locals())


def login_views(request):
    if request.method == 'POST':
        Users.objects.create(uname=request.POST['uname'],
                             upwd=request.POST['upwd'],
                             uemail=request.POST['uemail'])
    return render(request, 'index.html', locals())
