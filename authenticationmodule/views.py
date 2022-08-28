import json

from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view, schema
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend


class HelloView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        content = {'message': 'hello world'}
        return Response(content)


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        data = User.objects.all()
        response_data = UserListSerializer(data, many=True)
        return Response({"data": response_data.data})


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

