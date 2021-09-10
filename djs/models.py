from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title


class Info(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return str(self.name)