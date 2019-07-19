from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404, redirect

from .models import User, Book
from .serializers import UserSerializer, BookSerializer


class UserList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_list.html'
    serializer_class = UserSerializer

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer()
        return Response({'users': queryset, 'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('users')


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
