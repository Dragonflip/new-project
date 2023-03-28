from rest_framework import response, views, exceptions, status
from django.shortcuts import get_object_or_404
from menu.serializers import IngredienteSerializer
from menu.services import create_ingrediente, update_ingrediente
from menu.models import Ingredientes


class IngredienteApi(views.APIView):

    def get(self, request, id=None):
        ingredientes = Ingredientes.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        resp = response.Response(data=serializer.data)
        return resp

    def post(self, request):
        serializer = IngredienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            serializer.instance = create_ingrediente(data)
        except Exception as e:
            raise exceptions.ValidationError(e)

        resp = response.Response(data=serializer.data)
        resp.status_code = 201
        return resp

        
class IngredienteDetail(views.APIView):

    def get(self, request, pk):
        ingrediente = get_object_or_404(Ingredientes, id=pk)
        serializer = IngredienteSerializer(ingrediente)
        resp = response.Response(data=serializer.data)
        return resp

    def put(self, request, pk):
        instance = get_object_or_404(Ingredientes, id=pk)

        serializer = IngredienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            serializer.instance = update_ingrediente(data, instance)
        except Exception as e:
            raise exceptions.ValidationError(e)

        return response.Response(data=serializer.data)

    def patch(self, request, pk):
        instance = get_object_or_404(Ingredientes, id=pk)

        serializer = IngredienteSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            serializer.instance = update_ingrediente(data, instance)
        except Exception as e:
            raise exceptions.ValidationError(e)

        return response.Response(data=serializer.data)

    def delete(self, request, pk):
        ingrediente = get_object_or_404(Ingredientes, id=pk)
        ingrediente.delete()
        resp = response.Response(status=status.HTTP_204_NO_CONTENT)
        return resp
