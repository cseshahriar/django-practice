from django.db import models
from users.models import CustomUser

class CsvModel(models.Model):
    """ create objects from a csv file upload """
    file_name = models.FileField(upload_to='csvapp/')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"


PRODUCT_CHOICES = (
    ('TV', 'tv'),
    ('IPAD', 'ipad'),
    ('PLAYSTATION', 'playstation'),
)

class Sale(models.Model):
    product = models.CharField(max_length=200, choices=PRODUCT_CHOICES)
    salesman = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantitty = models.PositiveIntegerField()
    total = models.FloatField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.quantitty}"

    def save(self, *args, **kwargs):
        price = None
        
        if self.product == 'TV':
            price = 599.99
        elif self.product == 'IPAD':
            price = 400.00
        elif self.product == 'PLAYSTATION':
            price = 464.99
        else:
            pass

        self.total = price * self.quantitty
        super().save(*args, **kwargs)