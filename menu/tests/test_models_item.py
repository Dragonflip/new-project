import pytest
from menu.models import *


@pytest.mark.django_db
def test_nome_item():
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


def test_se_ingredientes_sao_veganos_item_e_vegano():
    ...
