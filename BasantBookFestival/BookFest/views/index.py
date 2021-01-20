from django.utils import timezone
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import os
import re
import datetime

from BookFest.models import Buyer, Publisher, Book
from BookFest.helpers.auth_helpers import create_user_from_email, create_publisher_from_email


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


@api_view(['POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def buyerRegister(request):
    if request.method == 'POST':
        data = request.data
        email = data['email']
        response = {	}
        try:
            buyer = Buyer.objects.get(email=email)
            return Response({'status': 0, 'message': 'Email already exists'})
        except:
            if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                return Response({'status': 0, 'message': 'Please enter a valid email address.'})
            try:
                PSRN = data['PSRN']
                is_professor = data['is_professor']
                user = create_user_from_email(email, PSRN, is_professor)
                try:
                    buyer = Buyer.objects.get(user=user)
                except:
                    return Response({'status': 0, 'message': 'Not a valid User Created'})
            except KeyError as missing_data:
                response = Response(
                    {'message': 'Data is Missing: {}'.format(missing_data)})
                return response
            return Response({
                'message': 'User '+'with '+'email '+email+' successfully created'
            })


@api_view(['POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def publisherRegister(request):
    if request.method == 'POST':
        data = request.data
        email = data['email']
        response = {	}
        try:
            publisher = Publisher.objects.get(email=email)
            return Response({'status': 0, 'message': 'Email already exists'})
        except:
            if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                return Response({'status': 0, 'message': 'Please enter a valid email address.'})
            try:
                name = data['name']
                user = create_publisher_from_email(email, name)
                try:
                    publisher = Publisher.objects.get(user=user)
                except:
                    return Response({'status': 0, 'message': 'Not a valid User Created'})
            except KeyError as missing_data:
                response = Response(
                    {'message': 'Data is Missing: {}'.format(missing_data)})
                return response
            return Response({
                'message': 'User '+'with '+'email '+email+' successfully created'
            })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bookRegister(request):
    data = request.data
    try:
        publisher = Publisher.objects.get(name=data.publisher_name)
    except:
        return Response({
            'message': 'Publisher ' + data.publisher_name + ' does not exist'
        })
    try:
        book = Book()
        book.title = data['title']
        book.author = data['author']
        book.edition = data['edition']
        book.year_of_publication = data['year_of_publication']
        book.price_foreign_currency = data['price_foreign_currency']
        book.price_indian_currency = data['price_indian_currency']
        book.ISBN = data['ISBN']
        book.description = data['description']
        book.discount = data['discount']
        book.save()
    except KeyError as missing_data:
        response = Response(
            {'message': 'Data is Missing: {}'.format(missing_data)})
        return response
