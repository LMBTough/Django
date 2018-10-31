from django.shortcuts import render
import os
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def add_page_views(request):
    if request.method == "POST":
        obj = request.FILES.get('page_file')
        with open(os.path.join(settings.BASE_DIR, 'static', 'pages',
                               obj.name), 'wb') as f:
            for chunk in obj.chunks():
                f.write(chunk)
        return HttpResponse('ok')
    else:
        return render(request, 'add_page.html')


def show_page_views(request, name):
    return render(request, os.path.join(settings.BASE_DIR, 'static', 'page',
                               name))