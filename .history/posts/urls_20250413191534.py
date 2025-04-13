
from django.urls import path

from posts.views import *


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
    path('files-list/', PostFileListView.as_view(), name = 'file-list'),
    path('User_Own_Post/<int:post_pk>/', User_Own_Post.as_view(), name='User-Own-Post'),
    #path('SinglePostView/<int:post_pk>/', SinglePostView.as_view(), name='single-post'),
    path('post/<int:post_pk>/', SinglePostView.as_view(), name='post-detail'),
]

    