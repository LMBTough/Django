from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def show_info(request):
    print(request)
    t = loader.get_template('index.html')
    html = t.render({
        'title': 'Music',
        'music_name': 'Little Apple',
        'music_author': 'chopstick',
        'music_singer': '筷子',
    })
    return HttpResponse(html)


def first_views(request):
    return render(request, 'first.html')


def second_views(request):
    return render(request, 'second.html')


def show_views(request, n1, n2):
    return render(request, 'third.html', {
        'title': int(n1) + int(n2)
    })
