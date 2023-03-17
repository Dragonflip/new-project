import pytest
from menu.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from fixtures import generate_test_image


@pytest.mark.django_db
def test_nome_item_media(generate_test_image):
    test_image = SimpleUploadedFile(
        name='test.png',
        content=generate_test_image.read(),
        content_type='image/png'
    )
    ItemMedia.objects.create(
        title="foto do pastel de frango", 
        imagem=test_image
    )
    item_media = ItemMedia.objects.last()
    print(item_media)
    assert item_media.__str__() == "foto do pastel de frango"
