import pytest
from menu.models import Ingredientes, Item


@pytest.fixture
@pytest.mark.django_db
def ingredientes_nao_veganos():
    ingrediente1 = Ingredientes.objects.create(
        nome="farinha de trigo",
        proteina=0,
        gordura=0,
        carboidrato=30,
        vegetal=False
    )
    ingrediente2 = Ingredientes.objects.create(
        nome="acucar",
        proteina=0,
        gordura=0,
        carboidrato=30,
        vegetal=False
    )
    return [ingrediente1, ingrediente2]


@pytest.fixture
@pytest.mark.django_db
def ingredientes_veganos():
    ingrediente1 = Ingredientes.objects.create(
        nome="farinha de trigo",
        proteina=0,
        gordura=0,
        carboidrato=30,
        vegetal=True
    )
    ingrediente2 = Ingredientes.objects.create(
        nome="acucar",
        proteina=0,
        gordura=0,
        carboidrato=30,
        vegetal=True
    )
    return [ingrediente1, ingrediente2]


@pytest.fixture
@pytest.mark.django_db
def item_com_ingredientes_veganos(ingredientes_veganos):
    item = Item.objects.create(
        nome="pastel de vento",
        descricao="um delicioso pastel de vento",
        tempo_preparacao=20,
        porcao=1,
        preco=10,
        alcoolico=False,
    )
    item.ingredientes.set(ingredientes_veganos)
    return item


@pytest.fixture
@pytest.mark.django_db
def item_com_ingredientes_nao_veganos(ingredientes_veganos, ingredientes_nao_veganos):
    #ingredientes veganos e nao veganos
    ingredientes = ingredientes_veganos + ingredientes_nao_veganos
    item = Item.objects.create(
        nome="pastel de vento",
        descricao="um delicioso pastel de vento",
        tempo_preparacao=20,
        porcao=1,
        preco=10,
        alcoolico=False,
    )
    item.ingredientes.set(ingredientes)
    return item


@pytest.mark.django_db
def test_se_ingredientes_sao_veganos_item_e_vegano(item_com_ingredientes_veganos):
    assert item_com_ingredientes_veganos.vegano == True


@pytest.mark.django_db
def test_se_algum_ingrediente_nao_e_vegano_o_item_nao_e_vegano(item_com_ingredientes_nao_veganos):
    assert item_com_ingredientes_nao_veganos.vegano == False


@pytest.mark.django_db
def test_item_sem_ingredientes_retorna_none_para_vegano():
    nome_item = "pastel de frango"
    Item.objects.create(
        nome=nome_item, 
        descricao="um delicioso pastel de frango",
        preco=10,
        tempo_preparacao=55,
        porcao=1,
        alcoolico=False
    )
    item = Item.objects.last()
    assert item.vegano == None


@pytest.mark.django_db
def test_nome_item():
    nome_item = "pastel de frango"
    Item.objects.create(
        nome=nome_item, 
        descricao="um delicioso pastel de frango",
        preco=10,
        tempo_preparacao=55,
        porcao=1,
        alcoolico=False
    )
    item = Item.objects.last()
    assert str(item) == f"Item: {nome_item}"
