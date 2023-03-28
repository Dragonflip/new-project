from rest_framework import serializers
from user.dto import UserDataClass


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, user):
        instance = super().to_internal_value(user)
        user_dc = UserDataClass(**instance)
        return user_dc


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
