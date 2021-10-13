from django.db import models
from django.utils import timezone 

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start = models.DateField(default=timezone.now)
    end = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)