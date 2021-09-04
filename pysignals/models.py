from django.db import models
from users.models import CustomUser

class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)