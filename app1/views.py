from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>vinay it is your lap tap</h1> ')
def second(request):
    return HttpResponse('<h1>hey vinay it is your second laptap</h1>')
