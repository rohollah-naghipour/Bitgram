
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from posts.models import *
from posts.serializers import PostSerializers, PostFileSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        print(posts)
        serializer = PostSerializers(posts, many= True)
        return Response(serializer.data)


class PostFileView(APIView):
    def get(self, request):
        files = PostFile.objects.all()
        print(files)
        serializer = PostFileSerializer(files, many = True)
        return Response(serializer.data)   


