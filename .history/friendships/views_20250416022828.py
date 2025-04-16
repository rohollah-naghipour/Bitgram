
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
        
        if Friendship.objects.filter(request_from=request.user,
                                      request_to=user).exists():
            return Response({'message': 'Friend request has already been sent'},
                             status=status.HTTP_409_CONFLICT)
        elif Friendship.objects.filter(request_from=user,
                                        request_to=request.user).exists():
            return Response({'message':'You have already received'
                             'a friend request from this user'}, 
                                 status=status.HTTP_409_CONFLICT)
        elif request.user == user:
            return Response({'message': 'You cannot send yourself a friend request'},
                             status=status.HTTP_400_BAD_REQUEST)

        Friendship.objects.create(request_from = request.user, request_to = user)
        return(Response({"detail": "Request sent"}, status = status.HTTP_200_OK)) 



class RequestsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:   
            requests = Friendship.objects.filter(request_to = request.user,
                                                  is_accepted = False)
        except Friendship.DoesNotExist:
            return(Response(status = status.HTTP_404_NOT_FOUND))       
        list_users = []
        for fr in requests:
            list_users.append(fr.request_from)
        
        serializer = UserListSerializer(list_users, many=True)
        return(Response(serializer.data, status = status.HTTP_200_OK))
    
        #serializer_2 = FriendshipSerializer(requests, many=True)
        #return(Response({'serializer_1': serializer_1.data,
                         #'serializer_2': serializer_2.data}))   

#difference in querying get == one instance with filter == instance list
class AcceptViews(APIView):
    
    def post(self, request):
        res_pk = request.data.get('user')
        try:
            user = User.objects.get(pk = res_pk)
            print(user)
            requests = Friendship.objects.get(request_from=user
                                              ,request_to=request.user,is_accepted=False)
        except (User.DoesNotExist, Friendship.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        requests.is_accepted = True
        requests.save()

        return Response({"detail": "Friend request accepted"})
                      


class FriendListView(APIView):
    def get(self, request):
        friends = Friendship.objects.filter(
            Q(request_from = request.user) | Q(request_to = request.user)
        )

        list_user = []
        print(request.user)
        for i in friends:
            list_user.append(i.request_to)
        
        serializer = UserListSerializer(list_user, many = True)     
        return(Response(serializer.data, status = status.HTTP_200_OK))    





#class RequestView(APIView):
    #def post(self, request):
        #user_id = request.data.get('user')
        #try:
            #user = User.objects.get(pk = user_id)
        #except User.DoesNotExist:
            #return(Response(status = status.HTTP_404_NOT_FOUND))
        
        #Friendship.objects.create(request_from = request.user, request_to = user)
        #return(Response({"detail": "Request sent"}, status = status.HTTP_200_OK))