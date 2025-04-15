

from friendships.models import Friendship
from users.models import Profile

from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar']
 
class UserListSerializer(serializers.ModelSerializer):
    #avatar = ProfileSerializer(read_only=True) 
    avatar = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.get(avatar))() 
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar'] 
        
     


#class UserListSerializer(serializers.ModelSerializer):
    #avatar = serializers.SerializerMethodField()

    #class Meta:
        #model = User
        #fields = ('id', 'username', 'avatar')

    #def get_avatar(self, instance):
        #if hasattr(instance, 'profile') and instance.profile.avatar:
            #return instance.profile.avatar.url
        #return ''