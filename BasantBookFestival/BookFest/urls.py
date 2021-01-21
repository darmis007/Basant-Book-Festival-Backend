from django.urls import path
from .views.auth import authenticate
from .views.index import index, sign_in, sign_out, buyerRegister, publisherRegister, bookRegister, getBooks, placeOrder, cancelOrder

urlpatterns = [
    path("", index, name='index'),
    path("auth/authenticate/", authenticate, name="auth-authenticate"),
    path("sign_in/", sign_in, name="sign_in"),
    path('logout/', sign_out, name="logout"),
    path('book/register/', bookRegister, name='bookRegister'),
    path('buyer/register/', buyerRegister, name='buyerRegister'),
    path('publisher/register/', publisherRegister, name='publisherRegister'),
    path('book/page/<int:page_number>/', getBooks, name='getBooks'),
    path('order/place/', placeOrder, name='placeOrder'),
    path('order/cancel/', cancelOrder, name='cancelOrder'),
]
