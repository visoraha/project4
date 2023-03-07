from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2(request):
    return HttpResponse('<h1>vinay it is your another app2 usage laptap<h1>') 
def second_app2(request):
    return HttpResponse('hey vinay it is your second app2 usage laptap ')