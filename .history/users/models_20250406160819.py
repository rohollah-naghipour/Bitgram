from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings


class Country(models.Model):
    pass

class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE),
    country = models.ForeignKey(to=Country, on_delete=models.SET_NULL), 
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True),
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/')




