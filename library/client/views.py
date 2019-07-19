from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Book
from .serializers import UserSerializer, BookSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserBooks(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = Book.objects.filter(user_id=user_id)
        return queryset

    def perform_create(self, request):
        serializer = BookSerializer(data=request.data)
        user = User.objects.get(id=self.kwargs['pk'])
        if serializer.is_valid():
            serializer.save(user=user)


class BookDetail(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer

    def get_object(self, *args, **kwargs):
        return Book.objects.get(pk=self.kwargs['id'])

    def put(self, request, *args, **kwargs):
        book = self.get_object(self.kwargs['id'])
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
