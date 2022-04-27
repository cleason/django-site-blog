from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to = 'blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    