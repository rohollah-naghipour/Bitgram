from django.urls import path

from friendships.views import *


urlpatterns = [
    path('users-list/', UserListView.as_view(), name = 'users-list'),  
    path('friend_request/', SendFriendRequestView.as_view(), name = 'friend-request' ),


    #path('request/', RequestView.as_view(), name = 'request-view'),
]
