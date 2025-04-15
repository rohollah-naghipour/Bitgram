

from friendships.models import Friendship

from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username'] 
        
     
class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['request_from','is_accepted']

        