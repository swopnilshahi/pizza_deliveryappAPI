from pyexpat import model
from .models import User
from rest_framework import serializers

class User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
