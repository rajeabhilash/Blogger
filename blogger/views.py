from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Duniya!</h1>")

def pratham(request):
    return HttpResponse("Hello, World! This is my Django app.")
