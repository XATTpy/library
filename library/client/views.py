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
        return redirect(request.path)


class UserBooks(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_books.html'
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['pk']
        queryset = Book.objects.filter(user_id=user_id)
        serializer = BookSerializer()
        return Response({'books': queryset, 'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        user = User.objects.get(id=self.kwargs['pk'])
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save(user=user)
        return redirect(request.path)


class BookDetail(generics.RetrieveUpdateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_detail.html'
    serializer_class = BookSerializer

    def get(self, *args, **kwargs):
        id = self.kwargs['id']
        book = Book.objects.get(id=id)
        serializer = BookSerializer
        return Response({'book': book, 'serializer': serializer})

    def post(self, request, *args, **kwargs):
        id = self.kwargs['id']
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save(book=book)
        return redirect(request.path)
