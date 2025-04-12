
from rest_framework import serializers
from posts.models import Post, PostFile, Comment, Like



class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'caption',  ,'is_active', 'is_public']    

        extra_kwargs = {
            'user': {"read_only": True}
        }





