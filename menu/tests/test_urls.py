import pytest
from django.urls import reverse, resolve

from menu.apis import IngredienteApi, IngredienteDetail, ItemApi, ItemDetail


#test ingrediente urls
def test_ingrediente_api():
    url = reverse("ingrediente")
    api = resolve(url)

    assert api.func.view_class == IngredienteApi

def test_ingrediente_detail():
    url = reverse("ingrediente_detail", kwargs={'pk': 1})
    api = resolve(url)

    assert api.func.view_class == IngredienteDetail

#test item urls
def test_item_api():
    url = reverse("item")
    api = resolve(url)

    assert api.func.view_class == ItemApi

def test_item_detail():
    url = reverse("item_detail", kwargs={'pk': 1})
    api = resolve(url)

    assert api.func.view_class == ItemDetail
