from django.http import HttpResponse
from django.shortcuts import render


def index(request):
#     return render(request, "hello/index.html", {name.capitalize()})

# def brian(request):
#     return HttpResponse("hello, Brian!")


def greet(request, name):
    return render(request, "hello/index.html", {name: name.capitalize()})
