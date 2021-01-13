from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('If you can see this, then the backend server is (hopefully) working. \n\t\t\t\t- Darsh Mishra')
