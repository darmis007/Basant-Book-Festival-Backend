from django.contrib import admin
from .models import Publisher, Book, Buyer, Order

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Buyer)
admin.site.register(Order)
