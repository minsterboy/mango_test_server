from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumb = models.ImageField(upload_to='thumbs/')
    img = models.ImageField(upload_to='images/')
