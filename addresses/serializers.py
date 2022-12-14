from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=50)
    number = serializers.IntegerField()
    complement = serializers.CharField(
        max_length=50, allow_null=True, allow_blank=True, default=None
    )
