from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from notesapi.models.users import User
from notesapi.serializers.userserializer import UserSerializer


class UserCreateListAPIView(APIView):
    def get(self, request):
        users = User.objects.filter(active=True)
        serializedUsers = UserSerializer(users, many=True)
        return Response(serializedUsers.data)

    def post(self, request):
        serializedUsers = UserSerializer(data=request.data)
        if(serializedUsers.is_valid()):
            serializedUsers.save()
            return Response(serializedUsers.data, status=status.HTTP_201_CREATED)
        return Response(serializedUsers.data, status=status.status.HTTP_400_BAD_REQUEST)
