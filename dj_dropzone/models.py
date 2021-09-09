from django.db import models


class Document(models.Model):
    upload = models.ImageField(upload_to='images/dropzone/')

    def __str__(self):
        return str(self.pk)


