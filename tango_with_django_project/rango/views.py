from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Just a message"}
    rend = render(request,'rango/indx.html',context=context_dict)
    #return HttpResponse("This is the first one, done this too many times<a href='/rango/about'>View about page</a>")
    return rend

def about(request):
    return HttpResponse("Well, you know this is about page, right? <a href='/rango/'>View index page</a>")