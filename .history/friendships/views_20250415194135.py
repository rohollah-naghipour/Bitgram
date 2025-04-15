
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from friendships.models import Friendship
from friendships.serializers import *

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        users = User.objects.filter(is_superuser= False,
                                    is_staff=False, is_active=True)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)




class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')

        user = User.objects.get(pk = user_id)
        
        if Friendship.objects.filter(request_from=request.user, request_to=user).exists():
            return Response({'message': 'Friend request has already been sent'},
                             status=status.HTTP_409_CONFLICT)
        elif Friendship.objects.filter(request_from=user, request_to=request.user).exists():
            return Response({'message':'You have already received'
                             'a friend request from this user'}, 
                                 status=status.HTTP_409_CONFLICT)
        elif request.user == user:
            return Response({'message': 'You cannot send yourself a friend request'},
                             status=status.HTTP_400_BAD_REQUEST)

        Friendship.objects.create(request_from = request.user, request_to = user)
        return(Response({"detail": "Request sent"}, status = status.HTTP_200_OK)) 



class RequestsListView(APIView):
    def get(self, request):

        requests = Friendship.objects.filter(request_to = request.user, is_accepted = False)
        #requests = Friendship.objects.all()

        serializer = FriendshipSerializer(requests, many=True)
        return(Response(serializer.data))






#class RequestView(APIView):
    #def post(self, request):
        #user_id = request.data.get('user')
        #try:
            #user = User.objects.get(pk = user_id)
        #except User.DoesNotExist:
            #return(Response(status = status.HTTP_404_NOT_FOUND))
        
        #Friendship.objects.create(request_from = request.user, request_to = user)
        #return(Response({"detail": "Request sent"}, status = status.HTTP_200_OK))
        
