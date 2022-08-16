from functools import partial
from types import ModuleType

from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from users import serializers

from .models import User
from .serializers import UserDetailSerializer, UserListSerializer


class UserView(APIView):
    def get(self, request: Request):
        users = User.objects.all()

        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request):

        serializer = UserDetailSerializer(data=request.data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        # Raise exception faz o if a cima.
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        serializer = UserDetailSerializer(user)

        return Response(serializer.data)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        serializer = UserDetailSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
