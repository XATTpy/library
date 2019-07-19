from rest_framework import serializers

from .models import User, Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'id']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'summary']
