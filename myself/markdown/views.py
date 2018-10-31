from django.shortcuts import render
import os
from django.http import HttpResponse
from django.conf import settings
import re
from .models import *
# Create your views here.


def show_markdown_views(request, name):
    path = Markdown.objects.get(name=name).path
    print(type(path))
    path = os.path.join(settings.BASE_DIR, 'upload', str(path))
    with open(path) as f:
        md = f.read()
    return render(request, 'show_md.html', {'md': md})



def add_markdown_views(request):
    if request.method == "POST":
        obj = request.FILES.get('md_file')
        with open(os.path.join(settings.BASE_DIR, 'static', 'md',
                               obj.name), 'wb') as f:
            for chunk in obj.chunks():
                f.write(chunk)
        return HttpResponse('ok')
    else:
        return render(request, 'add_md.html')

