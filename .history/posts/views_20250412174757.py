
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from posts.models import *
from posts.serializers import PostSerializers, PostFileSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        files = PostFile.objects.all()
        serializer_1 = PostFileSerializer(files, many = True)
        serializer_2 = PostSerializers(posts, many= True)
        return Response({
            'posts': serializer_1(posts, many=True),
            'files': serializer_2(files, many=True),
        })




class PostFileView(APIView):
    def get(self, request):
        files = PostFile.objects.all()
        serializer = PostFileSerializer(files, many = True)
        return Response(serializer.data)   


