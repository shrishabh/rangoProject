from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the first one, done this too many times")


# Create your views here.
