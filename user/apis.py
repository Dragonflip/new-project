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
