from rest_framework import serializers

from .models import User, Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['name', 'id', 'books']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'summary', 'owner']
