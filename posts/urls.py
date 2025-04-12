
from django.urls import path

from posts.views import PostListView


urlpatterns = [    
    path('posts-list/', PostListView.as_view(), name='posts-list'),
]

