from django.db import models

class MultiStepFormModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name