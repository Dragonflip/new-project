import pytest
from menu.models import Menu, MenuCategoria, MenuMedia
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
import shutil


@pytest.fixture()
def generate_test_image():
    file = BytesIO()
    image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
    image.save(file, "png")
    file.name = "test.png"
    file.seek(0)
    yield file
    shutil.rmtree("menu")


@pytest.mark.django_db
def test_menu_nome():
    menu = Menu.objects.create(
        nome="menu 1",
        descricao="o menu cheio de itens",
        disponivel=True
    )
    assert str(menu) == "menu 1"


@pytest.mark.django_db
def test_menu_pode_iniciar_sem_items():
    menu = Menu.objects.create(
        nome="menu 1",
        descricao="o menu cheio de itens",
        disponivel=True
    )
    assert menu.items.count() == 0


@pytest.mark.django_db
def test_menu_categoria_nome():
    menu_categoria = MenuCategoria.objects.create(
        nome="vegano",
        descricao="menu vegano",
    )
    assert str(menu_categoria) == "vegano"


@pytest.mark.django_db
def test_nome_item_media(generate_test_image):
    test_image = SimpleUploadedFile(
        name="test.png", content=generate_test_image.read(), content_type="image/png"
    )
    titulo_imagem = "menu de pasteis"
    MenuMedia.objects.create(title=titulo_imagem, imagem=test_image)
    menu_media = MenuMedia.objects.last()
    assert str(menu_media) == titulo_imagem
