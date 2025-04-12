
from django.urls import path

from posts.views import PostListView, PostFileSerializer


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
    path('files-list/', PostListView.as_view(), name = 'file-list'),
]

