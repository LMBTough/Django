
from django.http import HttpResponse


def fun_views(request):
    return HttpResponse("Hello Django")


def test(request, age, name):
    rqst = HttpResponse(age + name)
    return rqst
