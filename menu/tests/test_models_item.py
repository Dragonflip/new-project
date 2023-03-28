import pytest
from menu.models import *
from menu.tests.fixtures import (
        item_vegano,
        item_nao_vegano,
        ingrediente_vegano,
        ingrediente_nao_vegano,
        item_sem_ingrediente
)


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


@pytest.mark.django_db
def test_se_ingredientes_sao_veganos_item_e_vegano(item_vegano):
    assert item_vegano.vegano == True    


@pytest.mark.django_db
def test_se_ingredientes_nao_sao_veganos_item_nao_e_vegano(item_nao_vegano):
    assert item_nao_vegano.vegano == False

@pytest.mark.django_db
def test_se_nao_tem_ingredientes_item_vegano_retorna_none(item_sem_ingrediente):
    assert item_sem_ingrediente.vegano == None
