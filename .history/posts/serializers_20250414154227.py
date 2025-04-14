
from rest_framework import serializers
from posts.models import Post, PostFile, Comment, Like





class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields =  [ 'post', 'is_liked'] 
        extra_kwargs = {
            #'user': {"read_only": True},
            'post': {"read_only": True},
            'is_liked': {'required': False}
        }


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user','post', 'text', 'is_approved']
        extra_kwargs = {
            'user': {"read_only": True},
            'post': {"read_only": True}
        }



class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'caption','is_active', 'is_public']  
        extra_kwargs = {
            'user': {"read_only": True}
        }

class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFile
        fields = ['file', 'created_time']

        #extra_kwargs = {
            #'file': {"read_only": True},
            #'created_time': {'read_only': True}
        #}

#class SinglePost(serializers.ModelSerializer):
    #class Meta:
        #model = Post
        
