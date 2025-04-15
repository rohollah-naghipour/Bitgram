

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
        #fields = '__all__'
        fields = ['is_accepted', 'request_from', 'request_to']