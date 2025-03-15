from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World !")


def brian(request):
    return HttpResponse("Hello Brian !")
