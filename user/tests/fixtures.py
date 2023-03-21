import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def test_user():
    user = User(
        username="test_user",
        first_name="test_user",
        last_name="test_user",
        email="test_user",
    )
    user.set_password('test_user')
    user.save()
    return user
