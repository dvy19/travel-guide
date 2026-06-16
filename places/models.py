from django.db import models

from city.models import City

# Create your models here.
class PlaceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Place(models.Model):

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="places"
    )

    category = models.ForeignKey(
        PlaceCategory,
        on_delete=models.SET_NULL,
        null=True
    )

    name = models.CharField(max_length=200)

    description = models.TextField()

    address = models.TextField()

    latitude = models.FloatField()

    contact_number = models.CharField(
    max_length=15,
    blank=True
    )

    website = models.URLField(
    blank=True
    )

    entry_fee = models.DecimalField(
    max_digits=8,
    decimal_places=2,
    default=0
    )
    
    historical_significance = models.TextField(blank=True)

    longitude = models.FloatField()

    opening_time = models.TimeField()

    closing_time = models.TimeField()

    image_url = models.URLField(blank=True )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

'''
lat and long
Useful for:
Google Maps integration
Nearby places search
Route generation
'''


class Review(models.Model):

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"