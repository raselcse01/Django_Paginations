from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=400)
    publish_data = models.DateTimeField()
