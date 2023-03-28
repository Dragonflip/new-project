import pytest
from django.urls import reverse, resolve

from menu.apis import IngredienteApi, IngredienteDetail

def test_ingediente_api():
    url = reverse("ingrediente")
    api = resolve(url)

    assert api.func.view_class == IngredienteApi

def test_ingrediente_detail():
    url = reverse("ingrediente_detail", kwargs={'pk': 1})
    api = resolve(url)

    assert api.func.view_class == IngredienteDetail
