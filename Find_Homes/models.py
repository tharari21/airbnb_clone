from django.db import models
from django.db.models import Model
from django.utils import timezone
# from django.core import reverse
# Create your models here.


def Listing(Model):
    listing_id = models.AutoField(primary_key=True)
    location_id = models.ForeignKey(Locations, on_delete=models.CASCADE)
    host_id = models.ForeignKey()
    rating = models.IntegerField()
    price = models.DecimalField()
    description = models.CharField(max_length=300)
    images = models.ImageField()

    def __str__(self):
        return self.listing_id

    # listing_id (pk)
    # location_id (fk)
    # host_id (fk)
    # rating (out of 5)
    # price
    # description
    # availability


def Locations(Model):
    location_id = models.AutoField(primary_key=True)
    address1 = models.AddressField()
    address2 = models.AddressField()
    city = models.CityField()
    state = models.StateField()
    zip_code = models.ZipCode()


def Amenities():
    amenity_id = models.AutoField()
    amenity_description = models.CharField(max_length=200)

# def User(Model):
#     # User - id, name, date_of_birth, rating, phone number, email, ssn, credit_card_number, isHost - Maybe reserve certain ids for hosts.
#     user_id = models.IntegerField()
#     name = models.CharField()
#     dob = models.DateField()
#     rating = models.RatingField()
#     phone_number = models.PhoneNumberField()
#     email = models.EmailField()
#     ssn = models.CharField()
