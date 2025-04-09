from django.db import models
from django.conf import settings



class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE),
    title = models.CharField(max_length=50),
    caption = models.TextField(max_length=500),
    is_active = models.BooleanField(default=True),
    is_public = models.BooleanField(default=True),
    created_time = models.DateTimeField(auto_now_add=True),
    updated_time = models.DateTimeField(auto_now_add=True),

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title    
    

class PostFile(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE),
    file = models.ImageField(upload_to='media_posts/'),
    created_time = models.DateTimeField(auto_now_add = True),
    updated_time = models.DateTimeField(auto_now_add = True),


    class Meta: 
        db_table = 'postfiles'
        verbose_name = 'postfile'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    post = models.ForeignKey(to= Post, on_delete=models.PROTECT,
                              related_name='comments'), 
    text = models.TextField(max_length=320),
    created_time = models.DateTimeField(auto_now_add=True),
    updated_time = models.DateTimeField(auto_now_add=True),

    class Meta: 
        db_table = 'comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Like(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE),
    post = models.ForeignKey(to=Post, 
                             on_delete=models.PROTECT, related_name='likes'),
    is_like = models.BooleanField(default=True),
    created_time = models.DateTimeField(auto_now_add=True),
    updated_time = models.DateTimeField(auto_now_add=True),

    class Meta: 
        db_table = 'likes'
        verbose_name = 'like'
        verbose_name_plural = 'likes'

     




    