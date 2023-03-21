import pytest
from django.urls import reverse
from django.conf import settings
from rest_framework.test import APIClient
from .fixtures import test_user
import jwt


client = APIClient()

@pytest.mark.django_db
def test_registration_user():
    payload = {
        'username': 'test',
        'first_name': 'joao',
        'last_name': 'paulo',
        'email': 'admin@admin.com',
        'password': 'abc123'
    }

    url = reverse('register') 
    response = client.post(url, payload)

    assert response.status_code == 201


@pytest.mark.django_db
def test_se_username_ja_existe_retorna_500(test_user):
    payload = {
        'username': test_user.username,
        'first_name': 'joao',
        'last_name': 'paulo',
        'email': 'admin@admin.com',
        'password': 'abc123'
    }

    url = reverse('register') 
    response = client.post(url, payload)

    assert response.status_code == 500


@pytest.mark.django_db
def test_user_login_has_valid_token(test_user):
    payload = {
        'username': 'test_user',
        'password': 'test_user'
    }

    url = reverse('login')
    response = client.post(url, payload)
    token = str(response.cookies['jwt'])[16:-8]

    jwt_payload = jwt.decode(
        token,
        key=settings.JWT_SECRET,
        algorithms=['HS256',]
    )

    assert jwt_payload['user_id'] == test_user.id


@pytest.mark.django_db
def test_user_login_has_not_valid_credentials(test_user):
    payload = {
        'username': 'test_user',
        'password': 'user_test'
    }

    url = reverse('login')
    response = client.post(url, payload)
    assert response.status_code == 403


@pytest.mark.django_db
def test_login_com_usuario_nao_existente(test_user):
    payload = {
        'username': 'user_test',
        'password': 'test_user'
    }

    url = reverse('login')
    response = client.post(url, payload)
    assert response.status_code == 403
