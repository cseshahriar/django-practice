from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.TextField()

    def __str__(self):
        return str(self.title)