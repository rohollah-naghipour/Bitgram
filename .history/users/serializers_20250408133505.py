
from django.contrib.auth import get_user_model


from rest_framework import serializers
from rest_framework import UniqueValidator


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True, 
        validation = [UniqueValidator(queryset=User.objects.all())]),
    
    password_1 = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(required=True, write_only=True)

    class meta:
        model = User
        field = ['email', 'password_1', 'password_2', 'first_name', 'lastname']

        extra_kwargs = {   
            'first_name': {'required': False},
            'lastname': {'required': False}
        }  

      