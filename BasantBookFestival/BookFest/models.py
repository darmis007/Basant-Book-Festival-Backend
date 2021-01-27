from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


# Create your models here.


class Publisher(models.Model):
    """
    The Publisher 's details
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name="publisher_profile"
    )
    name = models.CharField(max_length=100)
    contact_no = PhoneNumberField(blank=True, null=True, unique=True)
    address = models.TextField(blank=True, null=True, max_length=2000)
    email = models.EmailField()
    logo = models.ImageField(
        upload_to='publisher_logos', null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"


class Buyer(models.Model):
    """
    The Buyer 's details
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="buyer_profile"
    )
    name = models.CharField(max_length=100)
    contact_no = PhoneNumberField(blank=True, null=True, unique=True)
    PSRN = models.CharField(blank=True, null=True,
                            max_length=2000, unique=True)
    email = models.EmailField()
    is_professor = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} + {self.PSRN}"


class Book(models.Model):
    """
    Model to save a Publisher 's Book
    Can be changed or updated
    """
    title = models.CharField(max_length=60)
    publisher = models.ForeignKey(
        Publisher,
        related_name="books",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    author = models.CharField(max_length=300, null=True, blank=True)
    edition = models.CharField(max_length=50, null=True, blank=True)
    year_of_publication = models.PositiveIntegerField(blank=True, null=True)
    price_foreign_currency = models.PositiveIntegerField(blank=True, null=True)
    price_indian_currency = models.PositiveIntegerField(blank=True, null=True)
    ISBN = models.CharField(max_length=20, null=True, blank=True)
    stock = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(0)])
    discount = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    expected_price = models.PositiveIntegerField(
        validators=[MinValueValidator(0)], blank=False, null=False)
    description = models.CharField(max_length=2000, blank=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    supplier = models.CharField(blank=True,null=True,max_length=500)
    thumbnail = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # For banning/unbanning products.
    visible = models.BooleanField(default=True)
    # For expiring products after given expiry period.
    expired = models.BooleanField(default=False)

    def to_dict(self):
        return {
            "pk": self.pk,
            "title": self.title,
            "edition": self.edition,
            "year_of_publication": self.year_of_publication,
            # "images": [im.url for im in self.images]
            "price_indian_currency": self.price_indian_currency,
            "price_indian_currency": self.price_foreign_currency,
            "publisher": self.publisher.name,
            "discount": self.discount,
            "expected_price": self.expected_price,
            "description": self.description,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "created_at": self.created_at,
        }

    def __str__(self):
        return f"{self.title} + {self.edition} + {self.publisher.name}"

    def save(self, *args, **kwargs):
        self.expected_price = self.price_indian_currency * \
            (1-((self.discount)/100))
        self.image = "http://covers.openlibrary.org/b/isbn/"+self.ISBN+"-M.jpg"
        self.thumbnail = "http://covers.openlibrary.org/b/isbn/"+self.ISBN+"-S.jpg"
        super().save(*args, **kwargs)


class Order(models.Model):
    """
    Model to save a user's order. 
    Users can add/delete orders from their cart.
    """
    book = models.ForeignKey(
        Book,
        related_name="orders",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    seller = models.ForeignKey(
        Publisher,
        related_name="orders",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    buyer = models.ForeignKey(
        Buyer,
        related_name="orders",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    recommended_to_library = models.BooleanField(default=False)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
