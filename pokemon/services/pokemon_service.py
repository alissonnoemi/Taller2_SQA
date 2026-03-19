import requests
from ..models import Pokemon

API_URL = "https://pokeapi.co/api/v2/pokemon?limit=30"

def get_pokemons():
    response = requests.get(API_URL)

    if response.status_code != 200:
        print(f"Error al obtener los pokemon: {response.status_code}")
        return []

    return response.json()["results"] 

def load_pokemons():
    if Pokemon.objects.count():
        return "Pokémon ya cargados"

    lista = get_pokemons()

    total = 0

    for item in lista:
        detalle = requests.get(item["url"]).json()

        Pokemon.objects.create(
    name=detalle["name"],
    image=detalle["sprites"]["front_default"],
    hp=detalle["stats"][0]["base_stat"],
    attack=detalle["stats"][1]["base_stat"],
    height=detalle["height"],
    weight=detalle["weight"],
    base_experience=detalle["base_experience"],
    types=", ".join([t["type"]["name"] for t in detalle["types"]]),
    abilities=", ".join([a["ability"]["name"] for a in detalle["abilities"]])
)

        total += 1

    return f"{total} pokemons cargados"