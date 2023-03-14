import pytest
from menu.models import *


def test_nome_ingrediente(db, django_db_setup):
    Ingredientes.objects.create(
        nome="peito de frango", proteina=32, gordura=2.5, carboidrato=0, vegetal=False
    )
    ingrediente = Ingredientes.objects.last()
    assert ingrediente.__str__() == "Ingrediente peito de frango"


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
    assert result.proteina == proteina
    assert result.gordura == gordura
    assert result.carboidrato == carboidrato
    assert result.vegetal == vegetal
