
from django.urls import path

from posts.views import PostListView, PostFileListView, SinglePostView, SinglePostView2


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
    path('files-list/', PostFileListView.as_view(), name = 'file-list'),
    path('posts/<int:pk>/', SinglePostView.as_view(), name='single-post'),
]

    