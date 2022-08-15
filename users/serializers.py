from recipes.serializers import RecipeSerializer
from rest_framework import serializers

from .models import Seasons


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    favorite_season = serializers.ChoiceField(
        choices=Seasons.choices, default=Seasons.DEFAULT
    )

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    recipes = RecipeSerializer(read_only=True, many=True)
