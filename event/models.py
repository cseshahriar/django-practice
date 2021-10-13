from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)