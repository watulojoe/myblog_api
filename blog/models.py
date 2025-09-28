from django.db import models
from django.db import models
from django.utils.text import slugify

# Create your models here.


class BlogPost(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200, unique=True)

    # URL-friendly version of the title
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    # Main content of the post
    content = models.TextField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Auto-generate slug if empty
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
