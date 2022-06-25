from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=42)
    image_url = models.CharField(max_length=500, default="")
    video_url = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
      
    class Meta:
        ordering = ["created_on"]



class Visual(models.Model):
    image_url = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]


class Comment(models.Model):
    content = models.CharField(max_length=42)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

