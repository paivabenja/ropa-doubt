from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'
