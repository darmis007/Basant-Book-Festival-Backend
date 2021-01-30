from django.urls import path
from .views.auth import authenticate
from .views.index import index, sign_in, sign_out, buyerRegister, publisherRegister, bookRegister, getBooks, getBook, getAllBooks, getAllSubjects, filterBooks, filterPublisherSubjectBooks, placeOrder, cancelOrder, myOrders, getPublishers, orderedExcel, orderedPublisherExcel

urlpatterns = [
    path("", index, name='index'),
    path("auth/authenticate/", authenticate, name="auth-authenticate"),
    path("sign_in/", sign_in, name="sign_in"),
    path('logout/', sign_out, name="logout"),
    path('book/register/', bookRegister, name='bookRegister'),
    path('buyer/register/', buyerRegister, name='buyerRegister'),
    path('publisher/register/', publisherRegister, name='publisherRegister'),
    path('publisher/list/', getPublishers, name='publisherList'),
    path('book/page/<int:page_number>/', getBooks, name='getBooks'),
    path('book/<int:book_id>/', getBook, name='getBook'),
    path('book/subjects/all/', getAllSubjects, name="allSubjects"),
    path('book/list/all/', getAllBooks, name="allBooks"),
    path('book/filter/<str:search_type>/', filterBooks, name='filterBook'),
    path('book/filter/<int:publisher>/<str:search_type>/',
         filterPublisherSubjectBooks, name='filterPublisherSubjectBooks'),
    path('order/place/', placeOrder, name='placeOrder'),
    path('order/cancel/', cancelOrder, name='cancelOrder'),
    path('order/my/', myOrders, name='myOrder'),
    path('order/master/excel/', orderedExcel, name='orderedExcel'),
    path('publisher/<int:publisher_id>/order/excel/',
         orderedPublisherExcel, name="orderedPublisherExcel"),
]
