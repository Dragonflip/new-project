import pytest
from django.urls import resolve, reverse

from user.apis import RegisterApi


def test_register_url():
    url = reverse("register")
    api = resolve(url)

    assert api.func.view_class == RegisterApi
