from django.shortcuts import render
from django.http import HttpResponse
import hashlib
# Create your views here.


def origin_views(request):
    return render(request, 'origin.html')
