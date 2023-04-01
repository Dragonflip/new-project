from rest_framework import serializers
from menu.models import Ingredientes, Item


class IngredienteSerializer(serializers.ModelSerializer):

    def to_internal_value(self, ingrediente):

        if self.instance and self.partial:
            ingrediente = {
                'nome': ingrediente.get('nome') or self.instance.nome,
                'proteina': ingrediente.get('proteina') or self.instance.proteina,
                'gordura': ingrediente.get('gordura') or self.instance.gordura,
                'carboidrato': ingrediente.get('carboidrato') or self.instance.carboidrato,
                'vegetal': ingrediente.get('vegetal') or self.instance.vegetal,
            }

        instance = super().to_internal_value(ingrediente)
        return instance

    class Meta:
        model=Ingredientes
        fields = '__all__'
        extra_kwargs = {
            'nome': {'validators': []},
        }

class ItemMediaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    imagem = serializers.ImageField()

class ItemSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(required=False, many=True)
    media = ItemMediaSerializer(required=False)

    def to_internal_value(self, item):

        if self.instance and self.partial:

            media = None
            if self.instance.media:
                media = {
                    'title': self.instance.media.title,
                    'imagem': self.instance.media.imagem
                }

            item_internal = {
                'nome': item.get('nome') or self.instance.nome,
                'descricao': item.get('descricao') or self.instance.descricao,
                'preco': item.get('preco') or self.instance.preco,
                'tempo_preparacao': item.get('tempo_preparacao') or self.instance.tempo_preparacao,
                'porcao': item.get('porcao') or self.instance.porcao,
                'alcoolico': item.get('alcoolico') or self.instance.alcoolico,
                'ingredientes': item.get('ingredientes') or [ingrediente for ingrediente in self.instance.ingredientes.all()]
            }

            if item.get('media') or media:
                item_internal['media'] = item.get('media') or media

        instance = super().to_internal_value(item)
        return instance

    class Meta:
        model = Item
        fields = '__all__'
