import pytest
from django.urls import reverse
from django.conf import settings
from rest_framework.test import APIClient
from menu.models import Ingredientes
from menu.tests.fixtures import ingrediente_vegano, ingrediente_nao_vegano
import jwt


client = APIClient()

@pytest.mark.django_db
def test_create_ingrediente():
    payload = {
        'nome': 'a',
        'proteina': 12,
        'carboidrato': 0,
        'gordura': 0,
        'vegetal': False
    }
    
    url = reverse('ingrediente')
    response = client.post(url, payload)

    assert response.status_code == 201


@pytest.mark.django_db
def test_se_ingrediente_ja_existir_retorna_400(ingrediente_vegano):

    payload = {
        'nome': ingrediente_vegano.nome,
        'proteina': 12,
        'carboidrato': 0,
        'gordura': 0,
        'vegetal': False
    }
    
    url = reverse('ingrediente')
    response = client.post(url, payload)

    assert response.status_code == 400

@pytest.mark.django_db
def test_se_todos_ingredientes_sao_retornados(ingrediente_vegano, ingrediente_nao_vegano):
    url = reverse('ingrediente')
    response = client.get(url)
    assert len(response.data) == 2


@pytest.mark.django_db
def test_se_ingrediente_criado_pode_ser_retornado(ingrediente_vegano):
    url = reverse('ingrediente_detail', kwargs={'pk':1})
    response = client.get(url)

    assert response.data.get('nome') == ingrediente_vegano.nome

@pytest.mark.django_db
def test_se_ingrediente_e_deletado_ele_e_removido_do_banco(ingrediente_vegano):
    url = reverse('ingrediente_detail', kwargs={'pk':1})
    response = client.delete(url)
    assert len(Ingredientes.objects.all()) == 0

@pytest.mark.django_db
def test_se_ingrediente_e_alterado_ele_modifica_no_banco(ingrediente_vegano):

    payload = {
        'nome': ingrediente_vegano.nome,
        'proteina': 12,
        'carboidrato': 0,
        'gordura': 0,
        'vegetal': False
    }

    url = reverse('ingrediente_detail', kwargs={'pk':1})
    response = client.put(url, payload)

    ingrediente = Ingredientes.objects.get(id=ingrediente_vegano.id)

    assert ingrediente.vegetal == payload.get('vegetal')

@pytest.mark.django_db
def test_se_mudar_nome_de_ingrediente_para_um_ingrediente_ja_existente_retorna_400(ingrediente_vegano, ingrediente_nao_vegano):

    payload = {
        'nome': ingrediente_vegano.nome,
        'proteina': 12,
        'carboidrato': 0,
        'gordura': 0,
        'vegetal': False
    }

    url = reverse('ingrediente_detail', kwargs={'pk':2})
    response = client.put(url, payload)

    assert response.status_code == 400

@pytest.mark.django_db
def test_patch_funciona_para_ingrediente(ingrediente_vegano):

    payload = {
        'nome': 'test_nome',
    }

    url = reverse('ingrediente_detail', kwargs={'pk':1})
    response = client.patch(url, payload)

    ingrediente = Ingredientes.objects.get(id=ingrediente_vegano.id)

    assert ingrediente.nome == payload.get('nome')

@pytest.mark.django_db
def test_patch_para_nome_ja_existente_retorna_400(ingrediente_vegano, ingrediente_nao_vegano):

    payload = {
        'nome': ingrediente_vegano.nome,
    }

    url = reverse('ingrediente_detail', kwargs={'pk':2})
    response = client.patch(url, payload)

    assert response.status_code == 400
