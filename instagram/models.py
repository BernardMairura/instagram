from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import Signal
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    profile_photo=models.ImageField()
    location=models.CharField(max_length=50,blank=True)
    birth_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return user



# class Image(models.Model):
#     image=models.ImageField(blank=True,null=True)
#     image_name=models.CharField(max_length=20)
#     image_caption=models.TextField(max_length=255)
#     image_profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
#     date_created=models.TimeField(auto_now_add=True,blank=True)
#     date_updated=models.TimeField(auto_now_add=True,blank=True)

#     def __str__(self):
#         return image_caption

