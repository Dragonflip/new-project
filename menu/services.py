from django.shortcuts import get_object_or_404
from menu.models import Ingredientes
from menu.dto import IngredienteDataClass


def create_ingrediente(ingrediente: IngredienteDataClass):
    instance = Ingredientes.objects.create(
        nome=ingrediente.nome,
        proteina=ingrediente.proteina,
        gordura=ingrediente.gordura,
        carboidrato=ingrediente.carboidrato,
        vegetal=ingrediente.vegetal
    )
    return IngredienteDataClass.from_instance(instance)

def update_ingrediente(data:IngredienteDataClass, instance:Ingredientes):
    instance.nome = data.nome
    instance.proteina = data.proteina
    instance.gordura = data.gordura
    instance.carboidrato = data.carboidrato
    instance.vegetal = data.vegetal
    instance.save()

    return IngredienteDataClass.from_instance(instance)
        
