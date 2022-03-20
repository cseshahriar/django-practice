from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    liked = models.ManyToManyField(User, related_name="liked")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"post pk: {self.pk}"

    @property
    def comments(self):
        """ reverse relationship """
        return self.comment_set.all()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
