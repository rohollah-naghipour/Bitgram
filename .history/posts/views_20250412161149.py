
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from posts.models import *
from posts.serializers import Postserializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = Postserializer(posts, many= True)
        return Response(serializer.data)









