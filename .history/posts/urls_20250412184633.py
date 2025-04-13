
from django.urls import path

from posts.views import PostListView, PostFileListView, SinglePostView


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
    path('files-list/', PostFileListView.as_view(), name = 'file-list'),
    path('post/<int:post_pk>/', SinglePostView.as_view(), name='post-detail'),

]