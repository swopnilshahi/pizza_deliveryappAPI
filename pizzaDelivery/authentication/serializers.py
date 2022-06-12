
from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=15)
    email = serializers.EmailField(
        max_length=255
    )
    phone_number = PhoneNumberField(allow_null=False,allow_blank=False)
    password = serializers.CharField(min_length=0)

    class Meta:
        model = User
        fields=['username', 'email', 'phone_number', 'password']

    def validate(self,attrs):
        username_exits = User.objects.filter(username=attrs['username']).exists()

        if username_exits:
            raise serializers.ValidationError (detail="Hello User with username exits ")

        email_exits = User.objects.filter(email=attrs['email']).exists()

        if email_exits:
            raise serializers.ValidationError(detail="User with email exits")

        phone_number_exits = User.objects.filter(phone_number=attrs['phone_number']).exists()

        if phone_number_exits:
            raise serializers.ValidationError(detail="User with phone_number exits")
        
        return super().validate(attrs)