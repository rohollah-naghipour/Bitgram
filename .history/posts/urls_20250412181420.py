
from django.urls import path

from posts.views import PostListView, PostFileListView


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
    path('files-list/', PostFileListView.as_view(), name = 'file-list'),
]

