import pytest
from PIL import Image
from io import  BytesIO
import shutil
import tempfile
from django.conf import settings
from menu.models import Ingredientes, Item


#ItemMedia fixtures
MEDIA_ROOT = tempfile.mkdtemp()
settings.MEDIA_ROOT = MEDIA_ROOT

@pytest.fixture()
def generate_test_image():
    file = BytesIO()
    image = Image.new('RGBA', size=(50,50), color=(155,0,0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    yield file
    shutil.rmtree(MEDIA_ROOT, ignore_errors=True)


#Item fixtures
@pytest.fixture()
def ingrediente_nao_vegano():
    ingrediente = Ingredientes.objects.create(
            nome='a',
            proteina=1,
            gordura=0,
            carboidrato=0,
            vegetal=False
        )
    return ingrediente


@pytest.fixture()
def ingrediente_vegano():
    ingrediente = Ingredientes.objects.create(
            nome='b',
            proteina=1,
            gordura=0,
            carboidrato=0,
            vegetal=True
        )
    return ingrediente


@pytest.fixture()
def item_vegano(ingrediente_vegano):
    item = Item.objects.create(
        nome='a',
        descricao='a',
        preco=0,
        tempo_preparacao=0,
        porcao=0,
        alcoolico=False
    )
    ingredientes = [ingrediente_vegano]
    item.ingredientes.set(ingredientes)
    return item


@pytest.fixture()
def item_nao_vegano(ingrediente_vegano, ingrediente_nao_vegano):
    item = Item.objects.create(
        nome='a',
        descricao='a',
        preco=0,
        tempo_preparacao=0,
        porcao=0,
        alcoolico=False
    )
    ingredientes = [ingrediente_vegano, ingrediente_nao_vegano]
    item.ingredientes.set(ingredientes)
    return item


@pytest.fixture()
def item_sem_ingrediente():
    item = Item.objects.create(
        nome='a',
        descricao='a',
        preco=0,
        tempo_preparacao=0,
        porcao=0,
        alcoolico=False
    )
    return item
