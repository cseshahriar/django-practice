from django.db import models

class CsvModel(models.Model):
    """ create objects from a csv file upload """
    file_name = models.FileField(upload_to='csvapp/')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"