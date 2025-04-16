from django.urls import path

from friendships.views import *


urlpatterns = [
    path('users-list/', UserListView.as_view(), name = 'users-list'),  
    path('friend_request/', SendFriendRequestView.as_view(), name = 'friend-request'),
    path('friend_request_list/', RequestsListView.as_view(), name = 'Requests-List'),
    path('Accept_request/', AcceptView.as_view(), name = 'accept-view'),

    #path('request/', RequestView.as_view(), name = 'request-view'),
]
