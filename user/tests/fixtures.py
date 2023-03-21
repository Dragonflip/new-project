import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def test_user():
    user = User.objects.create(
        username="teste_user",
        first_name="test_user",
        last_name="test_user",
        email="test_user",
        password="test_user",
    )
    return user
