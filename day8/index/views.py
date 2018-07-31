from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.


def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(**cd)
            return HttpResponse('Query OK!')


def origin_views(request):
    return render(request, 'origin.html', locals())
