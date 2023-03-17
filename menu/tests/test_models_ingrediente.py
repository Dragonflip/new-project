import pytest
from menu.models import *


@pytest.mark.django_db
def test_nome_ingrediente():
    nome = "peito de frango"
    Ingredientes.objects.create(
        nome=nome, proteina=32, gordura=2.5, carboidrato=0, vegetal=False
    )
    ingrediente = Ingredientes.objects.last()
    assert str(ingrediente) == nome
