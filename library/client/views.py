from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response({'users': users})
