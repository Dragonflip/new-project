from rest_framework import request, response, exceptions, views
from . import serializers as user_serializer
from . import services


class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            serializer.instance = services.create_user(data)
        except Exception as e:
            raise exceptions.APIException(str(e))

        resp = response.Response(data=serializer.data)
        resp.status_code = 201
        return resp


class LoginApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            user = services.get_user_from_username(data['username'])
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))

        resp = response.Response()

        if user.check_password(data['password']):
            token = services.create_token(user)
            resp.set_cookie(key='jwt', value=token)
        else:
            raise exceptions.AuthenticationFailed()

        return resp
