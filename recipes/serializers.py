from email.policy import default

from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    instructions = serializers.CharField(
        allow_null=True, allow_blank=True, default=None
    )
