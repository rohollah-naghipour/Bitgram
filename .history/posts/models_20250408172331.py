from django.db import models
from django.conf import settings



class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE),



