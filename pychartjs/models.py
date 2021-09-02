from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.money}'