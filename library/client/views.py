from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, Book
from .serializers import UserSerializer


class UserView(viewsets.ViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(book)
        return Response(serializer.data)
