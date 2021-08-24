from django.db import models


class Product(models.Model):
    """Product model """
    name = models.CharField(max_length=200)
    barcode = models.ImageField(upload_to='barcodes/')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        pass