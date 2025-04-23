# estates/models.py
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)

    def __str__(self):
        return self.city


class Property(models.Model):
    PROPERTY_TYPES = [
        ('HOUSE', 'House'),
        ('APARTMENT', 'Apartment'),
        ('CONDO', 'Condominium'),
        ('TOWNHOUSE', 'Townhouse'),
        ('LAND', 'Land'),
    ]
    name = models.CharField(max_length=256)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    square_feet = models.PositiveIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    has_garage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "property_type": self.property_type,
            "location": {
                "id": self.location.id,
                "city": self.location.city,
                "state": self.location.state,
                "country": self.location.country,
                "zip_code": self.location.zip_code
            },
            'square_feet': self.square_feet,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'has_balcony': self.has_balcony
        }
