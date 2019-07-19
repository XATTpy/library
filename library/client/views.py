from rest_framework import generics, viewsets

from .models import User, Book
from .serializers import UserSerializer, BookSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserBooks(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = Book.objects.filter(user=user_id)
        return queryset

    def perform_create(self, request):
        serializer = BookSerializer(data=request.data)
        user = User.objects.get(id=self.kwargs['pk'])
        if serializer.is_valid():
            serializer.save(user=user)


class BookUpdate(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.get()
