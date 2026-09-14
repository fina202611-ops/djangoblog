from django.db import models


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="published"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title