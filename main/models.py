from django.db import models
from django.contrib.auth.models import User, update_last_login
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True,  blank=True)
    profile_info = models.TextField(max_length=True, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='ok', blank=True, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(create_user_profile, sender=User)


