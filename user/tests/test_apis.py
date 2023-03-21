import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .fixtures import test_user


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
