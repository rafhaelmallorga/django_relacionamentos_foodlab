from types import ModuleType

from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from rest_framework.views import APIView, Request, Response, status

from .models import User


class UserView(APIView):
    def get(self, request: Request):
        users = User.objects.all()

        users_list = [model_to_dict(user) for user in users]

        return Response(users_list)

    def post(self, request: Request):
        user = User(**request.data)

        try:
            user.full_clean()
        except ValidationError as err:
            return Response(err.message_dict, status.HTTP_400_BAD_REQUEST)

        user.save()

        user_dict = model_to_dict(user)

        return Response(user_dict, status.HTTP_201_CREATED)
