from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        name = request.data.get('nane')
        serializer = UserSerializer(data=name)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({'success': 'User "{}" created successfully'.format(user_saved.name)})
