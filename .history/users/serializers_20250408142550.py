
from django.contrib.auth import get_user_model



from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True, 
        validations = [UniqueValidator(queryset=User.objects.all())]),
    
    password_1 = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(required=True, write_only=True)

    class meta:
        model = User
        field = ['email', 'password_1', 'password_2', 'first_name', 'lastname']

        extra_kwargs = {   
            'first_name': {'required': False},
            'lastname': {'required': False}
        }  
        
        def validate(self, attrs):
            if attrs['password_1'] != attrs['password_2']:
                raise serializers.ValidationError({
                'password': 'Passwords did not match.'})
        
            return super(RegisterSerializer, self).validate(attrs)

        def create(self, validate_data):
            user = User.objects.create(
                username = validate_data['username'],
                email = validate_data['email'],
                first_name = validate_data['first_name'],
                last_name = validate_data['last_name'] 
            )

            user.set_password(validate_data['password_1'])
            user.save()        


