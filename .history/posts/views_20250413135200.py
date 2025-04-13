
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
        serializer_1 =  PostSerializers(posts, many= True)
        serializer_2 = PostFileSerializer(files, many = True)
        return Response({
            'posts': serializer_1.data,
            'files': serializer_2.data,
            #'posts': serializer_1(posts, many=True),
            #'files': serializer_2(files, many=True),
        })


class PostFileListView(APIView):
    def get(self, request):
        files = PostFile.objects.all()
        serializer = PostFileSerializer(files, many = True)
        return Response(serializer.data)   



class SinglePostView(APIView):
    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False
    def get(self, request, post_pk):
        print(request.user)
        print(request.auth)
        post = self.get_post(post_pk)
        Response(status=status.HTTP_404_NOT_FOUND)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializers(post)
        return Response(serializer.data)



 















