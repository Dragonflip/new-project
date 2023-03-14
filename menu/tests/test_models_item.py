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


@pytest.mark.parametrize(
    "nome, descricao, preco, tempo_preparacao, porcao, alcoolico",
    [
        ("pastel de frango", "delicioso pastel de frango",10,  55, 1, False),
        ("pastel de carne", "delicioso pastel de carne",10, 55, 1, False),
    ],
)
def test_items_inseridos_corretamente(
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


def test_se_ingredientes_sao_veganos_item_e_vegano():
    ...
