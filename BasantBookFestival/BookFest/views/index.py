from django.utils import timezone
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import os
import re
import datetime


# Create your views here.


def index(request):
    return HttpResponse('If you can see this, then the backend server is (hopefully) working. \n\t\t\t\t- Darsh Mishra')

def sign_in(request):
    if request.user.is_anonymous:
        return render(request, 'sign_in.html')
    else:
        return redirect('/')

@login_required(login_url='api/sign_in')
def sign_out(request):
    logout(request)
    return redirect('api/sign_in')

