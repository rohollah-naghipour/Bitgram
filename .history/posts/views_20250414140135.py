
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


from posts.models import *
from posts.serializers import *

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        files = PostFile.objects.all()
        serializer_1 =  PostSerializers(posts, many= True)
        serializer_2 = PostFileSerializer(files, many = True)
        return Response({
            'posts': serializer_1.data,
            'files': serializer_2.data,
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
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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



class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False
        
    def get(self, request, post_pk):
        try:
            comment = Comment.objects.get(pk = post_pk)
        except Comment.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializers(comment)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, post_pk):
        post = self.get_post(post_pk)  
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print(request.data)
        serializer = CommentSerializers(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.sava(post = post)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    #def post(self, request, post_pk):
        #post = self.get_post(post_pk)
        #if not post:
            #return Response(status=status.HTTP_404_NOT_FOUND)
        #serializer = CommentSerializer(data=request.data)
        #if serializer.is_valid(raise_exception=True):
            #serializer.save(post=post, user=request.user)
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):
    def get(self, request, post_pk):
        try:
            like = Post.likes.filter(is_liked= True).count()
        except Post.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = LikeSerializers(like)
        return Response(serializer.data, status = status.HTTP_200_OK)  



    #def post(self, request):
        #serializer = PostSerializers(data=request.data)
        #if serializer.is_valid(raise_exception=True):
            #serializer.save(user = request.user)
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(status = status.HTTP_400_BAD_REQUEST) 
