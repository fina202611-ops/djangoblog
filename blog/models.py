from django.db import models
from django.contrib.auth.models import slugify

class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    status = models.CharField( max_length=10, choices=STATUS_CHOICES, default="published"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
