from django.contrib.auth.models import AbstractUser, Group
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("name of User"), blank=True, max_length=255)
    username = CharField(_("Username of User"), blank=True, max_length=255,unique=True,default="Username")
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})



class UserProfile(models.Model):
    role_choices = (
        ('SuperManager', 'SuperManager'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Mofid', 'Mofid'),
        ('Buyer', 'Buyer'),
    )
    
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user")
    about = models.TextField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to="profiles")
    nikname = models.CharField(max_length=255,blank=True,null=True)
    Introducing_video = models.CharField(max_length=255,blank=True,null=True)
    Country = models.CharField(max_length=255,blank=True,null=True)
    role = models.CharField(max_length=255, choices=role_choices, verbose_name='User Role',default='Buyer')
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.user.save()    
