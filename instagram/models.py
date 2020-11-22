from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime




# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    profile_photo=models.ImageField(upload_to='avatar/' ,null=True)
    location=models.CharField(max_length=50,blank=True)
    birth_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return user

    def save_Profile(self):
        self.save()

    def delete_Profile(self):
        self.delete()




class Image(models.Model):
    image=models.ImageField(upload_to='images/', blank=True,null=True)
    image_name=models.CharField(max_length=20)
    caption=models.TextField(max_length=255)
    image_profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created=models.TimeField(auto_now_add=True,blank=True)
    likes=models.PositiveIntegerField()
  

    def __str__(self):
        return image_caption


    def save_Image(self):
        self.save()
    
    def delete_Image(self):
        self.delete()



class Comment(models.Model):
    comment=models.TextField(max_length=150)
    post = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    date_commented=models.DateField(auto_now_add=True,blank=True)


    class Meta:
        ordering=['-date_commented']



    def __str__(self):
        return comment


    def save_Comment(self):
        self.save()


    def delete_Comment(self):
        self.delete()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()






