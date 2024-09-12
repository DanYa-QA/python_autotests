import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2603616a043ba8019066d6ae11b394a7'
pokemon_id = 70226
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}

body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_rename_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

# response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
# print(response_create_pokemon.json())
# pokemon_id = response_create_pokemon.json()['id']
# print(pokemon_id)

# response_rename_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename_pokemon)
# print(response_rename_pokemon.json())

# response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
# print(response_add_pokeball.json())