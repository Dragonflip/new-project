import pytest
from menu.models import *
from PIL import Image
from io import  BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
import shutil


@pytest.fixture()
def generate_test_image():
    file = BytesIO()
    image = Image.new('RGBA', size=(50,50), color=(155,0,0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    yield file
    shutil.rmtree('items')
        


def test_nome_item_media(db, django_db_setup, generate_test_image):
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
