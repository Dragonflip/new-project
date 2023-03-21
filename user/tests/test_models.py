import pytest
from user.models import Client
from .fixtures import test_user


@pytest.mark.django_db
def test_nome_cliente(test_user):
    cliente = Client.objects.filter(user=test_user).first()
    assert str(cliente) == 'test_user'
