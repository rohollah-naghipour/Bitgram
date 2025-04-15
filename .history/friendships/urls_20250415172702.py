from django.urls import path

from .views import UserListView


urlpatterns = [
    path('users-list/', UserListView.as_view(), name = 'users-list'),   
    path('request/', RequestView.as_view(), name = 'request-view')
]
