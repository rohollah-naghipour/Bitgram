from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.views import APIView    
from rest_framework.response import Response


from users.serializers import RegisterSerializer

import string
import random

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer 


class GeneratePassView(APIView):
    def get(self, request):
        num = 10
        password = ''
        for n in range(num):
            x = random.randint(0, 94)
            password += string.printable[x]
        return Response({"generaten password": password })
