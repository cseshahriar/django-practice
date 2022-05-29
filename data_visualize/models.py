from django.db import models


class Sale(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return str(self.price)
