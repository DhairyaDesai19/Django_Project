from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

