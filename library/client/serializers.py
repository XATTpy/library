from rest_framework import serializers

from .models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def create(self, varidated_data):
        return User.objects.create(**varidated_data)