import pytest
from menu.models import *


def test_nome_item(db, django_db_setup):
    Item.objects.create(
        nome="pastel de frango", 
        descricao="um delicioso pastel de frango",
        preco=10,
        tempo_preparacao=55,
        porcao=1,
        alcoolico=False
    )
    item = Item.objects.last()
    assert item.__str__() == "pastel de frango"


def test_nome_ingrediente(db, django_db_setup):
    Ingredientes.objects.create(
        nome="peito de frango", proteina=32, gordura=2.5, carboidrato=0, vegetal=False
    )
    ingrediente = Ingredientes.objects.last()
    assert ingrediente.__str__() == "Ingrediente peito de frango"


@pytest.mark.parametrize(
    "nome, descricao, preco, tempo_preparacao, porcao, alcoolico",
    [
        ("pastel de frango", "delicioso pastel de frango",10,  55, 1, False),
        ("pastel de carne", "delicioso pastel de carne",10, 55, 1, False),
    ],
)
def test_items_dbfixture(
    db, django_db_setup, nome, descricao, preco, tempo_preparacao, porcao, alcoolico
):
    result = Item.objects.create(
        nome=nome,
        descricao=descricao,
        preco=preco,
        tempo_preparacao=tempo_preparacao,
        porcao=porcao,
        alcoolico=alcoolico
    )
    assert result.nome == nome
    assert result.descricao == descricao
    assert result.preco == preco
    assert result.tempo_preparacao == tempo_preparacao
    assert porcao == porcao
    assert alcoolico == alcoolico


@pytest.mark.parametrize(
    "nome, proteina, gordura, carboidrato, vegetal",
    [
        ("peito de frango", 32, 2.5, 0, False),
        ("massa de pastel", 0, 0, 36, True),
    ],
)
def test_ingredientes_dbfixture(
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
