from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
