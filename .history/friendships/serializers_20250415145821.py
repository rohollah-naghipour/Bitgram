

from friendships.models import Friendship
from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']





#class UserListSerializer(serializers.ModelSerializer):
    #avatar = serializers.SerializerMethodField()

    #class Meta:
        #model = User
        #fields = ('id', 'username', 'avatar')

    #def get_avatar(self, instance):
        #if hasattr(instance, 'profile') and instance.profile.avatar:
            #return instance.profile.avatar.url
        #return ''