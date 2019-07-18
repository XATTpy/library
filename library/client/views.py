from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from .models import User
from .serializers import UserSerializer


class UserView(ListModelMixin, GenericAPIView):
    queryset = Uesr.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
