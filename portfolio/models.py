from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="portfolio_images/")
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog_images/")
    description = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
