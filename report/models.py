from django.db import models


class Report(models.Model):
    report = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return self.report
