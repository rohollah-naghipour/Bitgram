from django.contrib import admin

from posts.models import Post, PostFile, Comment, Like



admin.site.register(Post)
#admin.site.register(Comment, Like)