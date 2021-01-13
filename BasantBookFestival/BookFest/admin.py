from django.contrib import admin
from .models import Publisher, Department, Book, Buyer, Wishlist, Cart, Order

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Department)
admin.site.register(Book)
admin.site.register(Buyer)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order)
