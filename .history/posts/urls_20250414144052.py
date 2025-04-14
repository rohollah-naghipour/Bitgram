
from django.urls import path

from posts.views import *


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
    path('files-list/', PostFileListView.as_view(), name = 'file-list'),

    path('User_Own_Post/<int:post_pk>/', User_Own_Post.as_view(), name='User-Own-Post'),
    path('post/<int:post_pk>/', SinglePostView.as_view(), name='post-detail'),
    path('post/', SinglePostView.as_view(), name='post'),

    path('post/<int:post_pk>/comments/', CommentView.as_view(), name='comment'),
    path('post/<int:post_pk>/likes/', LikeView.as_view(), name='like'),
]

    #path('post/', PostView.as_view(), name='post'),
    #path('post/<int:post_pk>/', PostView.as_view(), name='post-detail'),
    #path('posts-list/', PostListView.as_view(), name='posts-list'),
    #path('post/<int:post_pk>/comments/', CommentView.as_view(), name='comment'),
    #path('post/<int:post_pk>/likes/', LikeView.as_view(), name='like'),
    