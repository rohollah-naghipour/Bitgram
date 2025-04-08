from rest_framework import serializers
from rest_framework.validators import UniqueValidator  # اصلاح import
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]  # اصلاح validators
    )
    
    password_1 = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(required=True, write_only=True)

    class Meta:  # اصلاح: Meta با حرف بزرگ
        model = User
        fields = ['email', 'password_1', 'password_2', 'first_name', 'last_name']  # اصلاح: fields و last_name

    extra_kwargs = {  # اصلاح: extra_kwargs
        'first_name': {'required': False},
        'last_name': {'required': False}  # اصلاح: last_name
    }

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:  # اصلاح: : به جای ;
            raise serializers.ValidationError({
                'password': 'Passwords did not match.'
            })
        return attrs  # نیازی به super() نیست چون ModelSerializer متد validate ندارد

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],  # معمولاً ایمیل به عنوان username استفاده می‌شود
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),  # استفاده از get برای فیلدهای اختیاری
            last_name=validated_data.get('last_name', '')
            password=validated_data['password_1']
        )
        return user
