from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveAPIView

from .models import User, Book
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return serializer.save()


class SingleUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
