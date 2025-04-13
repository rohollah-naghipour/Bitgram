
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


from posts.models import *
from posts.serializers import PostSerializers, PostFileSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        files = PostFile.objects.all()
        print(request.user)
        print(request.auth)
        serializer_1 =  PostSerializers(posts, many= True)
        serializer_2 = PostFileSerializer(files, many = True)
        return Response({
            'posts': serializer_1.data,
            'files': serializer_2.data,
            #'posts': serializer_1(posts, many=True),
            #'files': serializer_2(files, many=True),
        })




class SinglePostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request ,post_pk):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializers(post)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid:
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 



class User_Own_Post(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk, user=request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializers(post)
        return Response(serializer.data)


class PostFileListView(APIView):
    def get(self, request):
        files = PostFile.objects.all()
        serializer = PostFileSerializer(files, many = True)
        return Response(serializer.data)   

