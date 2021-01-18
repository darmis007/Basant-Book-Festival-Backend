from django.urls import path
from .views.auth import authenticate
from .views.index import index, sign_in, sign_out

urlpatterns = [
    path("", index, name='index'),
    path("auth/authenticate/", authenticate, name="auth-authenticate"),
    path("sign_in/", sign_in, name="sign_in"),
    path('logout/', sign_out, name="logout"),
]
