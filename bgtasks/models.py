from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return str(self.name)


class Document(models.Model):
    uploaded_file = models.FileField(upload_to='images/')
    expire_date = models.DateField()
    expire = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}-{self.expire}'