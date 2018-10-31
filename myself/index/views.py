from django.shortcuts import render
from django.http import HttpResponse
from markdown.models import *
import re
import hashlib
# Create your views here.


def origin_views(request):
    mk = []
    mn = []
    for i in Markdown.objects.order_by('check_day'):
        # print(str(i.path))
        path = os.path.join(settings.BASE_DIR, 'upload', str(i.path))
        with open(path) as f:
            md= f.read(100)
            # md = re.match(r'#([\s\S]+?)\n([\s\S]+)', w).group(2)
            mk.append((i.name, md))
    for i in Mindnode.objects.order_by('check_day'):
        mn.append(i.name)
    return render(request, 'index.html', {'mk': mk, 'mn': mn})
