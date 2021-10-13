from django.db import models
from django.utils import timezone 

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    starts_at = models.DateTimeField(default=timezone.now)
    ends_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)