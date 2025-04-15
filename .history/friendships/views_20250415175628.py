
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from friendships.models import Friendship
from friendships.serializers import UserListSerializer

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        users = User.objects.filter(is_superuser= False,
                                    is_staff=False, is_active=True)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class RequestView(APIView):
    def post(self, request):
        user_id = request.data.get('user')
        try:
            user = User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return(Response(status = status.HTTP_404_NOT_FOUND))
        
        Friendship.objects.create(request_from = request.user, request_to = user)

        return(Response({"detail": "Request sent"}, status = status.HTTP_200_OK))
        

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, FriendshipRequest
from .serializers import FriendshipRequestSerializer

class SendFriendRequestView(APIView):
    def post(self, request, receiver_id):
        sender = request.user   
        user_id = request.data.get('user')
        #receiver = get_object_or_404(User, id=receiver_id)

        
        if FriendshipRequest.objects.filter(request_from=sender, request_to=receiver).exists():
            return Response({'message': 'Friend request has already been sent.'}, status=status.HTTP_409_CONFLICT)
        elif FriendshipRequest.objects.filter(request_from=receiver, request_to=sender).exists():
            return Response({'message':'You have already received a friend request from this user.'}, status=status.HTTP_409_CONFLICT)
        #elif sender == receiver:
        elif sender == user_id:
            return Response({'message': 'You cannot send yourself a friend request..'}, status=status.HTTP_400_BAD_REQUEST)

        friend_request = FriendshipRequest(request_from=sender, request_to=user_id)
        friend_request.save()
        serializer = FriendshipRequestSerializer(friend_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
