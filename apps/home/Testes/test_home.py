from django.urls import reverse
from multiprocessing.connection import Client


from django.test import Client

def test_home_satatus_code(client:Client):
    resposta = client.get(reverse('home:home'))
    assert resposta.status_code == 200