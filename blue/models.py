from django.db import models


class Blue(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    app_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title