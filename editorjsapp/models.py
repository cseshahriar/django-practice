from django.db import models
from django_editorjs import EditorJsField
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = EditorJsField(
        editorjs_config={
            "tools": {
                "Image":{
                    "config": {
                        "endpoints": {
                            "byFile": "/imageUpload/",
                            "byUrl": "/imageUpload/",
                        },
                        "additionalRequestHeaders": [{"Content-Type": "application/form-data"}]
                    }
                },
                "Attaches": {
                    "config": {
                        "endpoint": "/fileUpload/"
                    },
                }
            }
        }
    )

    def __str__(self):
        return self.title