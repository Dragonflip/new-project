import pytest
from django.urls import resolve, reverse

from user.apis import RegisterApi, LoginApi


def test_register_url():
    url = reverse("register")
    api = resolve(url)

    assert api.func.view_class == RegisterApi


def test_login_url():
    url = reverse("login")
    api = resolve(url)

    assert api.func.view_class == LoginApi
