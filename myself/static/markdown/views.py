from django.shortcuts import render
import os
from django.http import HttpResponse

# Create your views here.
pwd = os.path.abspath('.') + '/markdown'


def show_markdown_views(request, name):
    with open(pwd + '/static/md/' + name + ".md") as f:
        md = f.read()
        return render(request, 'show_md.html', {'md': md})
