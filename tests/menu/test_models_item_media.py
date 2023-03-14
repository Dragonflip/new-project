import pytest
from menu.models import *
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
    shutil.rmtree("items")


@pytest.mark.django_db
def test_nome_item_media(generate_test_image):
    test_image = SimpleUploadedFile(
        name="test.png", content=generate_test_image.read(), content_type="image/png"
    )
    titulo_imagem = "pastel de frango"
    ItemMedia.objects.create(title=titulo_imagem, imagem=test_image)
    item_media = ItemMedia.objects.last()
    assert str(item_media) == f"Imagem: {titulo_imagem}"


