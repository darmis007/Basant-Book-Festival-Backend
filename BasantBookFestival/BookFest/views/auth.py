#import logging
from django.contrib.auth.models import User

from google.auth.transport import requests as google_requests
from google.oauth2 import id_token as googleIdToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from BookFest.helpers.auth_helpers import create_user_from_email, get_jwt_with_user
from BookFest.models import Buyer
# Set up logger.
#log = logging.getLogger("main")


@api_view(['POST'])
def authenticate(request):
    try:
        id_token = request.data["id_token"]
    except KeyError:
        return Response(
            {"error": "No id_token provided"}, status=status.HTTP_403_FORBIDDEN
        )

    id_info = googleIdToken.verify_oauth2_token(
        id_token, google_requests.Request())

    if id_info["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
        return Response(
            {"error": "Not a valid Google account"}, status=status.HTTP_403_FORBIDDEN
        )

    email = id_info["email"]
    try:
        first_name = id_info["given_name"]
        last_name = id_info["family_name"]
    except Exception as e:
        return Response({
            'message': e
        })

    # Login if user already exists.

    username, domain = email.split('@')

    if domain != "pilani.bits-pilani.ac.in":
        return Response(
            {"error": "Can only be accessed by Bits Mail"}, status=status.HTTP_403_FORBIDDEN
        )

    try:
        user = User.objects.get(username=username)
        is_professor = Buyer.objects.get(user = user).is_professor
    except User.DoesNotExist:
        return Response(
            {"error": "Technical Issue. Please try again or contact a library official"}, status=status.HTTP_403_FORBIDDEN
        )
    except Buyer.DoesNotExist:
        return Response(
            {"error": "Technical Issue. Please try again or contact a library official to enable Buyer status"}, status=status.HTTP_403_FORBIDDEN
        )


    token = get_jwt_with_user(user)

    return Response(
        {"token": token, "username": user.username,
            "first_name": first_name, "last_name": last_name, "is_professor":is_professor},
        status=status.HTTP_201_CREATED,
    )
