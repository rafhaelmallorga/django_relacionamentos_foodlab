from types import ModuleType

from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from rest_framework.views import APIView, Request, Response, status

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request):

        serializer = UserSerializer(data=request.data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        # Raise exception faz o if a cima.
        serializer.is_valid(raise_exception=True)

        user = User.objects.create(**serializer.validated_data)

        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
