from django.core.files.uploadedfile import SimpleUploadedFile
from fixtures import generate_test_image
import pytest
from menu.models import Menu, MenuCategoria, MenuMedia


@pytest.mark.django_db
def test_nome_menu():
    nome = 'test_nome'
    menu = Menu.objects.create(
        nome=nome,
        descricao = 'a',
        disponivel=True
    )
    assert str(menu) == nome


@pytest.mark.django_db
def test_nome_menu_categoria():
    nome = 'test_nome'
    menu_categoria = MenuCategoria.objects.create(
        nome=nome,
        descricao='a'
    )
    assert str(menu_categoria) == nome


@pytest.mark.django_db
def test_nome_menu_media(generate_test_image):
    nome = 'test_nome'
    test_image = SimpleUploadedFile(
        name='test.png',
        content=generate_test_image.read(),
        content_type='image/png'
    )
    menu_media = MenuMedia.objects.create(
        nome=nome,
        imagem=test_image
    )
    assert str(menu_media) == nome
