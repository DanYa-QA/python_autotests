import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2603616a043ba8019066d6ae11b394a7'
TRAINER_ID = '4933'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_line_trainer_id():
    response_2 = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_2.json()["data"][0]["trainer_id"] == TRAINER_ID

