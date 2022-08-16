from addresses.models import Address
from addresses.serializers import AddressSerializer
from recipes.serializers import RecipeSerializer
from rest_framework import serializers

from .models import Seasons, User


class UserListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    favorite_season = serializers.ChoiceField(
        choices=Seasons.choices, default=Seasons.DEFAULT
    )

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    favorite_season = serializers.ChoiceField(
        choices=Seasons.choices, default=Seasons.DEFAULT
    )

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    time_between = serializers.SerializerMethodField()

    def get_time_between(self, obj: User):
        time_diff = obj.updated_at - obj.created_at
        return str(time_diff)

    recipes = RecipeSerializer(read_only=True, many=True)
    address = AddressSerializer()

    def create(self, validated_data: dict) -> User:

        address_data = validated_data.pop("address")
        user_obj = User.objects.create(**validated_data)

        Address.objects.create(**address_data, user=user_obj)

        return user_obj

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
