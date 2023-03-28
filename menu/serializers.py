from rest_framework import serializers
from menu.dto import IngredienteDataClass 



class IngredienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()
    proteina = serializers.DecimalField(max_digits=5, decimal_places=2)
    gordura = serializers.DecimalField(max_digits=5, decimal_places=2)
    carboidrato = serializers.DecimalField(max_digits=5, decimal_places=2)
    vegetal = serializers.BooleanField()

    def to_internal_value(self, user):
        if not self.instance:
            instance = super().to_internal_value(user)
            ingrediente_dc = IngredienteDataClass(**instance)
        else:
            ingrediente_dc = IngredienteDataClass(
               nome=user.get('nome') or self.instance.nome,
               gordura=user.get('gordura') or self.instance.gordura,
               carboidrato=user.get('carboidrato') or self.instance.carboidrato,
               proteina=user.get('proteina') or self.instance.proteina,
               vegetal=user.get('vegetal') or self.instance.vegetal
            )
        return ingrediente_dc

