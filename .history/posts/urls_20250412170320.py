
from django.urls import path

from posts.views import PostListView, PostFileView


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
    path('files-list/', PostFileView.as_view(), name = 'file-list'),
]

