import pytest
from menu.models import *


@pytest.mark.django_db
def test_nome_ingrediente():
    nome_ingrediente = "peito de frango"
    Ingredientes.objects.create(
        nome=nome_ingrediente, proteina=32, gordura=2.5, carboidrato=0, vegetal=False
    )
    ingrediente = Ingredientes.objects.last()
    assert str(ingrediente) == f"Ingrediente: {nome_ingrediente}"


@pytest.mark.parametrize(
    "nome, proteina, gordura, carboidrato, vegetal",
    [
        ("carne desfiada", 32, 2.5, 0, False),
        ("peito de frango", 32, 2.5, 0, False),
        ("massa de pastel", 0, 0, 36, True),
    ],
)
def test_ingredientes_inseridos_corretamente(
    db, django_db_setup, nome, proteina, gordura, carboidrato, vegetal
):
    result = Ingredientes.objects.create(
        nome=nome,
        proteina=proteina,
        gordura=gordura,
        carboidrato=carboidrato,
        vegetal=vegetal,
    )
    calorias = proteina * 4 + carboidrato * 4 + gordura * 9
    assert result.calorias == calorias
