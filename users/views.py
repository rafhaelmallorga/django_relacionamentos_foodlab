from types import ModuleType

from django.forms.models import model_to_dict
from rest_framework.views import APIView, Request, Response, status

from .models import User


class UserView(APIView):
    def get(self, request: Request):
        users = User.objects.all()

        users_list = [model_to_dict(user) for user in users]

        return Response(users_list)

    def post(self, request: Request):
        ...
