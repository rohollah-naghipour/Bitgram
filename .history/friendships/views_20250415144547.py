
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
                                    is_staff=False, is_active=True,)
        print(users)
        serializer = UserListSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
