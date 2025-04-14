from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.views import APIView    
from rest_framework.response import Response
from rest_framework import status

from users.serializers import RegisterSerializer

import string
import random

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer 


class GeneratePassView(APIView):
   
    def post(self, request, num):
        list_random = ['A','B','C','D','E','F','G','H','I','J',
         'K','L','M','N','O','P','Q','R','S',
         'T','U','V','W','X','Y','Z','a','b','c',
         'd','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z',
        '0','1','2','3','4','5','6','7','8','9','!','@',
        '$','%','^','&','*','(',')','=','+','{','}','[',']','|',
        '/',':',';','<','>','?','/']
        if num < 10 or num > 25:
            return Response({"The password is less than"
            " tenor greater than twenty-five.": num},
            status = status.HTTP_400_BAD_REQUEST)
        password = ''
        for n in range(num):
            password += random.choice(list_random)
        return Response({"generaten_password": password })


  